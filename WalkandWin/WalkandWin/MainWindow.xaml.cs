using System.IO;
using System.Text.Json;
using System.Windows;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Threading;

namespace WalkandWin
{
    public partial class MainWindow
    {
        private DispatcherTimer _timer;
        private List<Person> _users;
        private Person _currentUser;
        private string[] _quotes;
        private Random _random;
        public MainWindow()
        {
            InitializeComponent();
            _random = new Random();
            _quotes = [
                "Ny dag, nye muligheter!",
                "Grip dagen med begge hender!",
                "Hver dag er en ny sjanse til å skinne.",
                "Alt er mulig for den som tror.",
                "La i dag være starten på noe stort.",
                "Hver dag er en ny mulighet til å gjøre noe fantastisk.",
                "Fyll dagen med glede og optimisme.",
                "Skap dine egne solskinnsdager.",
                "Hver dag er en gave, bruk den klokt.",
                "La i dag være en dag du vil huske.",
                "Ditt smil kan lyse opp verden."
            ];
            _users = LoadFromFile();
            _currentUser = _users.Find(user => user.Name == "Chris");
            if (_currentUser == null)
            {
                _currentUser = new Person("Chris", 0, false,true,DateTime.Today);
                _users.Add(_currentUser);
                SaveToFile();
                StatusMessage.Text = "Bruker opprettet";
            }
            
            if (_currentUser.ResetDate != DateTime.Today)
            {
                _currentUser.NotPressed();
                _currentUser.SetNotFinished();
                _currentUser.SetDate(DateTime.Today);
                SaveToFile();
                StatusMessage.Text = "Ny dag lagt til";
            }
            Message.Text = _quotes[_random.Next(_quotes.Length -1)];
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
            var remainingTime = _currentUser.DueTime - DateTime.Now;
            CountdownText.Text = remainingTime.ToString(@"hh\:mm\:ss");
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            if (remainingTime.TotalMinutes <= 30)
            {
                CountdownText.Foreground = Brushes.Red;
            }
            else
            {
                CountdownText.Foreground = Brushes.Black;
            }

            if (DateTime.Now >= _currentUser.StartTime &&
                DateTime.Now <= _currentUser.EndTime)
            {
                DoneButton.Visibility = _currentUser.IsDone ? Visibility.Collapsed : Visibility.Visible;
            }
            else
            {
                DoneButton.Visibility = Visibility.Collapsed;
            }
            if (DateTime.Now >= _currentUser.DueTime)
            {
                if (!_currentUser.IsDone && !_currentUser.Finished)
                {
                    _currentUser.MinusPoints();
                    Message.Text = "Oouf kanskje i morgen!";
                    _currentUser.SetFinished();
                    SaveToFile();
                }
                _currentUser.ResetDueTime();
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
        private void GearIcon_Click(object sender, MouseButtonEventArgs e)
        {
            var settingsWindow = new SettingsWindow(_currentUser) { Owner = this };
            settingsWindow.ShowDialog();
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
                    StatusMessage.Text = $"Bruker er lastet inn";
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
