"""
Created on Thu Jan 25 10:12:23 2024

@author: naveen
"""

import sys
import pandas as pd
import mariadb_connection

class model_scoring():
    
    def query_execute(cur1,query,filename):
        # Open a cursor to perform database operations
        
        # Getting data from claim_data table
        cur.execute(query)
        claim_data = cur1.fetchall()
        claim_data_col = [i[0] for i in cur.description]

        claim_data_df = pd.DataFrame(claim_data, columns=claim_data_col)
        claim_data_df.to_csv('output/' + str(filename), index=False)
        
    
    def model_scoring_fun():
        try:
            # Check the connection status
            connection=mariadb_connection.db_connection
            
            if connection:
                
                print("MariaDB Connection successfull...")
                
                # Open a cursor to perform database operations
                cur = connection.cursor()
        
                # Getting data from claim_data table
                
                claim_model_query="""select  cc.claim_number, cc.trigger_type, cc.claim_type
                               from cholams.claim cc Join cholams.model_meter mm on
                               cc.claim_number=mm.claim_number
                               where mm.created_date >= convert('2023-09-01 00:00:00.000', datetime)"""
                               
                claim_model=query_execute(cur,claim_model_query,'claim_data.csv')
                
                ###############################################################################
        
                # Getting data from claim_output table
                claim_output_query="""select
                       CO.claim_number,
                       CO.policy_no,
                       CO.final_claim_amount_before_capping,
                       CO.policy_type_values,
                       CO.mode_of_claim_values,
                       CO.hospital_state_name,
                       CO.intermediary_mapping_values,
                       CO.final_risk_grade_vf
                       from  cholams.claim_output CO JOIN cholams.model_meter MM ON CO.claim_number=MM.claim_number
                       where MM.created_date >= convert('2023-09-01 00:00:00.000', datetime)"""
                       
                claim_output=query_execute(cur,claim_output_query,'claim_output.csv')

                               
                ##############################################################################
        
                # Getting data from model_meter table
                
                model_meter="""select claim_number, api_return_code , created_date from cholams.model_meter
                               where created_date >= convert('2023-09-01 00:00:00.000', datetime)"""
        
                claim_output=query_execute(cur,claim_output_query,'model_meter.csv')
                
                # Make the changes to the database persistent
                # conn.commit()
        
                # Close cursor and communication with the database
                cur.close()
                connection.close()
            else:
                print('Connection database failed...')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    model_scoring.model_scoring_fun()