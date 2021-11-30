using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ExcelGH.forms
{
    public partial class frmSettings : Form
    {
        public frmSettings()
        {
            InitializeComponent();
            label1.Text = access.dbPath;
        }
        
        private void button2_Click(object sender, EventArgs e)
        {
            SaveFileDialog saveFileDialog1 = new SaveFileDialog();  
            saveFileDialog1.Filter = "CSV Files|*.csv|All Files|*.*";
            saveFileDialog1.Title = "Save";
            saveFileDialog1.DefaultExt = "ExportDataBase.csv";
            saveFileDialog1.RestoreDirectory = true;

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                lblPath.Text = "status : "+saveFileDialog1.FileName+ " exported Successfully ...";
            }
            
        }

        private void button1_Click(object sender, EventArgs e)
        {

            using (OpenFileDialog openFileDialog = new OpenFileDialog())
            {
                //openFileDialog.InitialDirectory = "c:\\";
                openFileDialog.Filter = "csv files (*.csv)|*.csv|All files (*.*)|*.*";
                //openFileDialog.FilterIndex = 2;
                openFileDialog.RestoreDirectory = true;

                if (openFileDialog.ShowDialog() == DialogResult.OK)
                {
                    lblPath.Text = "status : " + openFileDialog.FileName + " imported Successfully ...";
                  
                }
            }
            
            //MessageBox.Show(fileContent, "File Content at path: " + filePath, MessageBoxButtons.OK);
        }

       
    }
}
