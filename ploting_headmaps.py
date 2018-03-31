
def main():
    import plotly
    import plotly.plotly as py
    import pandas as pd
    from config import api_key
    import json
    from states_trans import states
    
    def per_year(data_all_years,year):
        df_state = df_state.loc[df_state['year']==year,:]
        df_grouped_flu = df_state.groupby(['state']).sum()
        df_grouped_flu = df_grouped_flu[['flu_cases','flu_percent']]
        
        # Accumulated Vaccination Rate and Cases in each state
        df_grouped_vac = df_state.loc[df_state['week']==52,['state','vac_percent','vaccinations']]
        df_grouped_vac.head()
        
        # Creat a State Abrreviation table

        #code = [states[i] for i in df_plot['state'].unique()]
        state_name_df = pd.DataFrame({"state":df_state['state'].unique()})
        state_name_df['code'] = [states[i] for i in state_name_df['state']]
        state_name_df.head()
        
        # Add corresponding State code to grouped flu table
        #abbrv = list(state_name_df['code'])
        df_grouped_flu['code'] = list(state_name_df['code'])
        df_grouped_flu['code'] =df_grouped_flu['code'].astype(str)
        df_grouped_flu.tail(10)
        
        # Add coresponding State code to grouped flu table
        df_grouped_vac['code'] = list(state_name_df['code'])
        df_grouped_vac['code'] = df_grouped_vac['code'].astype(str)
        df_grouped_vac.head(10)
        
        # df with both flu and vaccinations
        pd_flu_vac = pd.merge(df_grouped_vac, df_grouped_flu, on="code")
        
        return (pd_flu_vac)
    
    
    def ploting_heatmaps(pd_flu_vac,year)
        

        