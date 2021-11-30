using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.OleDb;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using DocumentFormat.OpenXml.Drawing.Charts;
using Microsoft.Office.Interop.Excel;

namespace ExcelGH.forms
{
    public partial class frmReporting : Form
    {
        public frmReporting()
        {
            InitializeComponent();
            SendMessage(txtSearch.Handle, EM_SETCUEBANNER, 0, "Search");
        }

        private const int EM_SETCUEBANNER = 0x1501;
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        private static extern Int32 SendMessage(IntPtr hWnd, int msg, int wParam, [MarshalAs(UnmanagedType.LPWStr)] string lParam);

        private void frmReporting_Load(object sender, EventArgs e)
        {
            string aa = access.dbPath;
            System.Data.DataTable dt =  access.ReadCell(aa);
            dataGridView1.DataSource = dt;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string aa = access.dbPath;
            System.Data.DataTable dt = access.ReadCell(aa);
            dataGridView1.DataSource = dt;
            txtSearch.Clear();
        }

        private void txtSearch_TextChanged(object sender, EventArgs e)
        {
            string aa = access.dbPath;
            System.Data.DataTable dt = access.ReadCell(aa);
            System.Data.DataTable res = new System.Data.DataTable();
            dataGridView1.DataSource = dt;
            string searchValue = txtSearch.Text;
            try
            {
                System.Data.DataRow ro;
                var row0 = from row in dt.AsEnumerable() where row[0].ToString().ToLower().Contains(searchValue)  select row;

                //row0.Last(from row in dt.AsEnumerable() where row[0].ToString().ToLower().Contains(searchValue) select row);
                var row1 = from row in dt.AsEnumerable() where row[1].ToString().ToLower().Contains(searchValue) select row;
                var row2 = from row in dt.AsEnumerable() where row[2].ToString().ToLower().Contains(searchValue) select row;
                var row3 = from row in dt.AsEnumerable() where row[3].ToString().ToLower().Contains(searchValue) select row;
               
                if (row0.Count() != 0)
                {
                    res.Merge(row0.CopyToDataTable());
                }
                if (row1.Count() != 0)
                {
                    res.Merge(row1.CopyToDataTable());
                }
                if (row2.Count() != 0)
                {
                    res.Merge(row2.CopyToDataTable());
                }
                if (row3.Count() != 0)
                {
                    res.Merge(row3.CopyToDataTable());
                }
                dataGridView1.DataSource = res;

                
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
    
        
    
    

