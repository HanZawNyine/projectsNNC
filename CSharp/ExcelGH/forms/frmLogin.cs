using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExcelGH.forms
{
    public partial class frmLogin : Form
    {
        

        public frmLogin()
        {
            InitializeComponent();
            SendMessage(txtUserName.Handle, EM_SETCUEBANNER, 0, "Username");
            SendMessage(txtPassword.Handle, EM_SETCUEBANNER, 0, "Password");
            this.Text = string.Empty;
            this.ControlBox = false;
            this.MaximizedBounds = Screen.FromHandle(this.Handle).WorkingArea;

        }
        private const int EM_SETCUEBANNER = 0x1501;
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);

        private void button1_Click(object sender, EventArgs e)
        {

            //string username = txtUserName.Text;
            //string password = txtPassword.Text;
            //txtUserName.Clear();
            //txtPassword.Clear();

            //lblStatus.Text = "username :"+username + " password :" + password;
           
            this.Hide();
            checkingDb main = new checkingDb();
            main.ShowDialog();
            this.Close();
            



        }

        [DllImport("user32.DLL", EntryPoint = "ReleaseCapture")]
        private extern static void ReleaseCapture();
        [DllImport("user32.DLL", EntryPoint = "SendMessage")]
        private extern static void SendMessage(System.IntPtr hWnd, int wMsg, int wParam, int lParam);

        private void frmLogin_Load(object sender, EventArgs e)
        {

        }

        private void frmLogin_MouseDown(object sender, MouseEventArgs e)
        {
            ReleaseCapture();
            SendMessage(this.Handle, 0x112, 0xf012, 0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
