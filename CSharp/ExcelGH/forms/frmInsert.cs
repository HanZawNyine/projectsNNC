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
    public partial class frmInsert : Form
    {
        public frmInsert()
        {
            InitializeComponent();
            SendMessage(txtName.Handle, EM_SETCUEBANNER, 0, "Name");
            SendMessage(txtAmount.Handle, EM_SETCUEBANNER, 0, "Amount");
            SendMessage(txtAddress.Handle, EM_SETCUEBANNER, 0, "Address");
        }
        private const int EM_SETCUEBANNER = 0x1501;
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);

        private void txtName_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
