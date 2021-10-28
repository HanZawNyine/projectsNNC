using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp1.frmProducts
{
    public partial class frmProducts : Form
    {
        public frmProducts()
        {
            InitializeComponent();
            panel11.BackColor = Color.FromArgb(27, 31, 44);
            panel13.BackColor = Color.White;
            panel15.BackColor = Color.FromArgb(27, 31, 44);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            panel11.BackColor = Color.White;
            panel13.BackColor = Color.FromArgb(27, 31, 44);
            panel15.BackColor = Color.FromArgb(27, 31, 44);
            // button4.Font = FontStyle.Bold;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            panel11.BackColor = Color.FromArgb(27, 31, 44);
            panel13.BackColor =  Color.White;
            panel15.BackColor = Color.FromArgb(27, 31, 44);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            panel11.BackColor = Color.FromArgb(27, 31, 44);
            panel13.BackColor = Color.FromArgb(27, 31, 44);
            panel15.BackColor = Color.White;
        }

       
    }

        
}
