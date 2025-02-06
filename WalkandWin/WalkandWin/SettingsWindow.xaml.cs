using System.Windows;

namespace WalkandWin
{
    public partial class SettingsWindow
    {
        private Person _currentUser;

        public SettingsWindow(Person currentUser)
        {
            InitializeComponent();
            _currentUser = currentUser;
            StartTimeTextBox.Text = _currentUser.StartTime.ToString("HH:mm");
            DueTimeTextBox.Text = _currentUser.DueTime.ToString("HH:mm");
            EndTimeTextBox.Text = _currentUser.EndTime.ToString("HH:mm");
        }

        private void SaveButton_Click(object sender, RoutedEventArgs e)
        {
            _currentUser.UpdateStartTime(StartTimeTextBox.Text);
            _currentUser.UpdateDueTime(DueTimeTextBox.Text);
            _currentUser.UpdateEndTime(EndTimeTextBox.Text);
            Close();
        }
    }
}