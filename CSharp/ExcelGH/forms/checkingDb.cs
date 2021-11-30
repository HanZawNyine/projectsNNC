using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExcelGH.forms
{
    public partial class checkingDb : Form
    {
        public checkingDb()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {                
                access.dbPath = textBox1.Text;
                //MessageBox.Show(access.dbPath);
                this.Hide();
                frmMain ma = new frmMain();
                ma.ShowDialog();
                this.Close();

            }
            else
            {

                using (OpenFileDialog openFileDialog = new OpenFileDialog())
                {
                    //openFileDialog.InitialDirectory = "c:\\";
                    openFileDialog.Filter = "excel files (*.csv)|*.xlsx|All files (*.*)|*.*";
                    //openFileDialog.FilterIndex = 2;
                    openFileDialog.RestoreDirectory = true;

                    if (openFileDialog.ShowDialog() == DialogResult.OK)
                    {
                        textBox1.Text = openFileDialog.FileName;
                    }
                }

            }
        }
    }
}
