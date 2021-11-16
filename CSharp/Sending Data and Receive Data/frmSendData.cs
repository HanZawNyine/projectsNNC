using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO.Ports;

namespace _1_Sending_Data
{
    public partial class frmSendData : Form
    {
        string sendWidth;
        string dataIN;

        public frmSendData()
        {
            InitializeComponent();
        }

        private void frmSendData_Load(object sender, EventArgs e)
        {
            string[] ports = SerialPort.GetPortNames();
            cboComPort.Items.AddRange(ports);
            cboComPort.SelectedIndex = 0;

            checkBox5.Checked = false;
            serialPort1.DtrEnable = false;

            checkBox6.Checked = false;
            serialPort1.RtsEnable = false;

            button3.Enabled = true;
            checkBox1.Checked = true;

            checkBox4.Checked = true;
            checkBox3.Checked = false;
            sendWidth = "Write";

            button2.Enabled = false;

            checkBox9.Checked = true;
            checkBox10.Checked = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                serialPort1.PortName = cboComPort.Text;
                serialPort1.BaudRate = Convert.ToInt32(cboBaudRate.Text);
                serialPort1.DataBits = Convert.ToInt32(cboDataBit.Text);
                serialPort1.StopBits = (StopBits)Enum.Parse(typeof(StopBits), cboStopBits.Text);
                serialPort1.Parity = (Parity)Enum.Parse(typeof(Parity), cboParity.Text);
               
                serialPort1.Open();
                progressBar1.Value = 100;
                label8.Text = "ON";
                //button1.Enabled = false;
                //button2.Enabled = true;

            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
            button1.Enabled = false;
            button2.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(serialPort1.IsOpen)
            {
                serialPort1.Close();
                progressBar1.Value = 0;
                button1.Enabled = true;
                button2.Enabled = false;
                label8.Text = "OFF";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if(serialPort1.IsOpen)
            {
                if(sendWidth == "Write")
                {
                    serialPort1.Write(txtDataSend.Text);
                }
                else
                {
                    serialPort1.WriteLine(txtDataSend.Text);
                }
                //txtDataSend.Clear();
            }
        }

        private void checkBox5_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox5.Checked)
            {
                serialPort1.DtrEnable = true;
                MessageBox.Show("DTR Enable", "Warning", MessageBoxButtons.OK,MessageBoxIcon.Warning);
            }
            else
            {
                serialPort1.DtrEnable = false;
            }
        }

        private void checkBox6_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox6.Checked)
            {
                serialPort1.RtsEnable = true;
                MessageBox.Show("RTS Enable", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                serialPort1.RtsEnable = false;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if(txtDataSend.Text != "")
            {
                txtDataSend.Text = "";
            }
        }

        private void txtDataSend_TextChanged(object sender, EventArgs e)
        {
            int dataLength = txtDataSend.TextLength;
            lblDataLength.Text = string.Format("{0:00}",dataLength);
       
            if(checkBox2.Checked)
            {
                txtDataSend.Text = txtDataSend.Text.Replace(Environment.NewLine, "");
            }
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox1.Checked)
            {
                button3.Enabled = true;
                checkBox2.Checked = false;
            }
            else
            {
                button3.Enabled = false;
            }
        }

        private void checkBox2_KeyDown(object sender, KeyEventArgs e)
        {
           
        }

        private void checkBox3_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox3.Checked)
            {
                sendWidth = "WriteLine";
                checkBox4.Checked = false;
            }
        }

        private void checkBox4_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox4.Checked)
            {
                sendWidth = "Write";
                checkBox3.Checked = false;
            }
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox2.Checked)
            {
                checkBox1.Checked = false;
            }
        }

        private void txtDataSend_KeyDown(object sender, KeyEventArgs e)
        {
            if (checkBox2.Checked)
            {
                checkBox1.Checked = false;
                if (e.KeyCode == Keys.Enter)
                {
                    if (serialPort1.IsOpen)
                    {
                        if (sendWidth == "Write")
                        {
                            serialPort1.Write(txtDataSend.Text);
                        }
                        else
                        {
                            serialPort1.WriteLine(txtDataSend.Text);
                        }
                        //txtDataSend.Clear();
                        //MessageBox.Show("HI");
                    }
                }
            }
        }

        private void serialPort1_DataReceived(object sender, SerialDataReceivedEventArgs e)
        {
            dataIN = serialPort1.ReadExisting();
            this.Invoke(new EventHandler(ShowData));
        }

        private void ShowData(object sender, EventArgs e)
        {
            int dataLength = dataIN.Length;
            label7.Text = string.Format("{0:00}", dataLength);
            if(checkBox10.Checked)
            {
                textBox1.Text = dataIN;
            }else if(checkBox9.Checked)
            {
                textBox1.Text += dataIN;
            }

        }

        private void checkBox10_CheckedChanged(object sender, EventArgs e)
        {
            if(checkBox10.Checked)
            {
                checkBox10.Checked = true;
                checkBox9.Checked = false;
            }
            else
            {
                checkBox9.Checked = true;
            }
        }

        private void checkBox9_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox9.Checked)
            {
                checkBox9.Checked = true;
                checkBox10.Checked = false;
            }
            else
            {
                checkBox10.Checked = true;
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if(textBox1.Text != "")
            {
                textBox1.Text = "";
            }
        }
    }
}
