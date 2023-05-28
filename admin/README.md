提供streamlit之外的数据库修改权限

## 重置API Key 使用次数
```shell
python -m admin.update_key_times key
```
## 查看API Key 详情
```shell
python -m admin.get_key_info key
```
## 手动增加API Key 
```shell
python -m admin.gen_key_sys utils@163.com

```