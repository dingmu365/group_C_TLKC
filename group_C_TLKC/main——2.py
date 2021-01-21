from p_tlkc_privacy.privacyPreserving import privacyPreserving

event_log = "Sepsis_Cases_ Event_Log.xes"

L = [8]
C = [0.2]
K = [80]
K2 = [0.7,0.8,0.9]
sensitive = ['disease','age']
#sensitive = []
T = ["minutes"]
cont = []
bk_type = "relative" #set, multiset, sequence, relative

privacy_aware_log_dir = "xes_results"
privacy_aware_log_path = "test_sepsis_str_relative.xes"

pp = privacyPreserving(event_log, "example")
print(pp)
result = pp.apply(T, L, K, C, K2, sensitive, cont, bk_type, privacy_aware_log_dir, privacy_aware_log_path)

print(result)
