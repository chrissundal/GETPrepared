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

        public MainWindow()
        {
            InitializeComponent();
            var random = new Random();
            string[] quotes = [
                "Ny dag, nye muligheter!",
                "Grip dagen med begge hender!",
                "Hver dag er en ny sjanse til å skinne.",
                "Alt er mulig for den som tror.",
                "La i dag være starten på noe stort.",
                "Ny mulighet til å gjøre noe fantastisk.",
                "Fyll dagen med glede og optimisme.",
                "Skap dine egne solskinnsdager.",
                "Hver dag er en gave, bruk den klokt.",
                "La i dag være en dag du vil huske.",
                "Ditt smil kan lyse opp verden."
            ];
            _users = LoadFromFile();
            _currentUser = _users.Find(user => user.Name == "Chris")!;
            if (_currentUser == null)
            {
                _currentUser = new Person("Chris", 0, false,true, DateTime.Today, DateTime.Today.AddHours(11).AddMinutes(30), DateTime.Today.AddHours(12).AddMinutes(15),DateTime.Today.AddHours(12).AddMinutes(15));
                _users.Add(_currentUser);
                SaveToFile();
                StatusMessage.Text = "Bruker opprettet";
            }
            
            if (_currentUser.ResetDate != DateTime.Today)
            {
                _currentUser.NotPressed();
                _currentUser.SetNotNewUser();
                _currentUser.SetDate(DateTime.Today);
                SaveToFile();
                StatusMessage.Text = "Ny dag lagt til";
            }
            Message.Text = quotes[random.Next(quotes.Length -1)];
            StartTimer();
        }

        private void StartTimer()
        {
            _timer = new DispatcherTimer();
            _timer.Interval = TimeSpan.FromSeconds(1);
            _timer.Tick += Timer_Tick!;
            _timer.Start();
        }

        private void Timer_Tick(object sender, EventArgs e)
        {
            var remainingTime = _currentUser.DueTime - DateTime.Now;
            CountdownText.Text = remainingTime.ToString(@"hh\:mm\:ss");
            PointsText.Text = $"Poeng: {_currentUser.Points}";
            CountdownText.Foreground = remainingTime.TotalMinutes <= 30 ? Brushes.Red : Brushes.Black;

            if (DateTime.Now >= _currentUser.StartTime &&
                DateTime.Now <= _currentUser.EndTime)
            {
                DoneButton.Visibility = _currentUser.IsDone ? Visibility.Collapsed : Visibility.Visible;
            }
            else
            {
                DoneButton.Visibility = Visibility.Collapsed;
            }

            Console.WriteLine(_currentUser.DueTime);
            Console.WriteLine(DateTime.Now);
            if (DateTime.Now >= _currentUser.DueTime)
            {
                if (!_currentUser.IsDone)
                {
                    _currentUser.MinusPoints();
                    Message.Text = "Oouf kanskje i morgen!";
                    _currentUser.PressedDone();
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
            var users = new List<Person>();
            try
            {
                if (File.Exists("db.json"))
                {
                    var json = File.ReadAllText("db.json");
                    users = JsonSerializer.Deserialize<List<Person>>(json) ?? [];
                    StatusMessage.Text = "Bruker er lastet inn";
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Feil ved lasting av brukere: {ex.Message}");
            }
            return users;
        }

        private void SaveToFile()
        {
            try
            {
                var json = JsonSerializer.Serialize(_users);
                StatusMessage.Text = "Bruker lagret";
                File.WriteAllText("db.json", json);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Feil ved lagring av brukere: {ex.Message}");
            }
        }
    }
}
