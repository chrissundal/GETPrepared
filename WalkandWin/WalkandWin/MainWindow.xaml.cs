using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Media;
using System.Windows.Threading;

namespace WalkandWin
{
    public partial class MainWindow : Window
    {
        private DispatcherTimer _timer;
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
                _currentUser = new Person("Chris", 0, false,false,new DateTime());
                _users.Add(_currentUser);
            }
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            _dueTime = DateTime.Today.AddHours(12).AddMinutes(15);
            if (_currentUser.ResetDate != DateTime.Today)
            {
                _currentUser.NotPressed();
                _currentUser.SetNotFinished();
                _currentUser.SetDate(DateTime.Today);
                SaveToFile();
                StatusMessage.Text = "Ny dag lagt til";
            }
            Message.Text = "Ny dag, nye muligheter!";
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
            var remainingTime = _dueTime - DateTime.Now;
            CountdownText.Text = remainingTime.ToString(@"hh\:mm\:ss");

            if (remainingTime.TotalMinutes <= 30)
            {
                CountdownText.Foreground = Brushes.Red;
            }
            else
            {
                CountdownText.Foreground = Brushes.Black;
            }

            if (DateTime.Now >= DateTime.Today.AddHours(11).AddMinutes(30) &&
                DateTime.Now <= DateTime.Today.AddHours(12).AddMinutes(15))
            {
                DoneButton.Visibility = _currentUser.IsDone ? Visibility.Collapsed : Visibility.Visible;
            }
            else
            {
                DoneButton.Visibility = Visibility.Collapsed;
                Message.Text = "Ny dag, nye muligheter!";
            }
            if (DateTime.Now >= _dueTime)
            {
                if (!_currentUser.IsDone && !_currentUser.Finished)
                {
                    _currentUser.MinusPoints();
                    Message.Text = "Oouf kanskje i morgen!";
                    _currentUser.SetFinished();
                    SaveToFile();
                }
                _dueTime = DateTime.Today.AddDays(1).AddHours(12).AddMinutes(15);
            }
        }

        private void DoneButton_Click(object sender, RoutedEventArgs e)
        {
            _currentUser.PlussPoints();
            Message.Text = "Godt jobba!";
            _currentUser.PressedDone();
            DoneButton.Visibility = Visibility.Collapsed;
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
