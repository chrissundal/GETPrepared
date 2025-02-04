using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Threading;

namespace WalkandWin
{
    public partial class MainWindow : Window
    {
        private DispatcherTimer _timer;
        private DateTime _targetTime;
        private DateTime _dueTime;
        private List<Person> _users;
        private Person _currentUser;

        public MainWindow()
        {
            InitializeComponent();
            _users = LoadFromFile();
            _currentUser = _users.Find(user => user.Name == "Chris");
            if (_currentUser == null)
            {
                _currentUser = new Person("Chris", 0, false,false);
                _users.Add(_currentUser);
            }
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            _targetTime = DateTime.Today.AddHours(11).AddMinutes(45);
            _dueTime = DateTime.Today.AddHours(12).AddMinutes(15);
            if (DateTime.Now > _targetTime)
            {
                _targetTime = _targetTime.AddDays(1);
                _dueTime = _dueTime.AddDays(1);
            }
            StartTimer();
        }

        private void StartTimer()
        {
            _timer = new DispatcherTimer();
            _timer.Interval = TimeSpan.FromSeconds(1);
            _timer.Tick += Timer_Tick;
            _timer.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            var remainingTime = _targetTime - DateTime.Now;
            CountdownText.Text = remainingTime.ToString(@"hh\:mm\:ss");

            if (DateTime.Now >= DateTime.Today.AddHours(11).AddMinutes(45) && DateTime.Now <= DateTime.Today.AddHours(12).AddMinutes(15))
            {
                DoneButton.Visibility = _currentUser.IsDone ? Visibility.Collapsed : Visibility.Visible;
                _currentUser.SetNotFinished();
                var timeLeft = _dueTime - DateTime.Now;
                DueText.Text = timeLeft.ToString(@"hh\:mm\:ss");
                DueText.Visibility = _currentUser.IsDone ? Visibility.Collapsed : Visibility.Visible;
            }
            else if (DateTime.Now > DateTime.Today.AddHours(12).AddMinutes(15) && !_currentUser.Finished)
            {
                if (!_currentUser.IsDone)
                {
                    _currentUser.MinusPoints();
                    PointsText.Text = $"Poeng: {_currentUser.Points}";
                    Message.Text = "Oouf kanskje i morgen!";
                    SaveToFile();
                }
                _currentUser.NotPressed();
                DoneButton.Visibility = Visibility.Collapsed;
                _targetTime = _targetTime.AddDays(1);
                _dueTime = _dueTime.AddDays(1);
                _currentUser.SetFinished();
                SaveToFile();
            }
            else
            {
                Message.Text = "Ny dag, nye muligheter!";
                DueText.Visibility = Visibility.Collapsed;
            }
        }

        private void DoneButton_Click(object sender, RoutedEventArgs e)
        {
            _currentUser.PlussPoints();
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            Message.Text = "Godt jobba!";
            _currentUser.PressedDone();
            DoneButton.Visibility = Visibility.Collapsed;
            SaveToFile();
        }

        private void ResetButton_Click(object sender, RoutedEventArgs e)
        {
            _currentUser.Reset();
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            SaveToFile();
        }

        private List<Person> LoadFromFile()
        {
            const string filePath = "db.json";
            try
            {
                if (File.Exists(filePath))
                {
                    var json = File.ReadAllText(filePath);
                    var users = JsonSerializer.Deserialize<List<Person>>(json);
                    StatusMessage.Text = "Brukere lastet inn";
                    return users;
                }
                else
                {
                    return [];
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Feil ved lasting av brukere: {ex.Message}");
                return [];
            }
        }

        private void SaveToFile()
        {
            const string filePath = "db.json";
            try
            {
                var json = JsonSerializer.Serialize(_users);
                StatusMessage.Text = "Bruker lagret";
                File.WriteAllText(filePath, json);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Feil ved lagring av brukere: {ex.Message}");
            }
        }
    }
}
