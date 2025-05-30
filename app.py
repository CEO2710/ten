import streamlit as st
import sys
import subprocess
import os

# 设置页面配置
st.set_page_config(
    page_title="Surgical Risk Prediction",
    page_icon="🏥",
    layout="wide"
)

# 强制安装 joblib
st.warning("Installing required dependencies...")

try:
    import joblib
    st.success("✅ joblib is already installed")
except ImportError:
    st.info("⏳ joblib not found. Installing now...")
    try:
        # 使用系统pip安装
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install", 
            "--disable-pip-version-check",
            "--no-cache-dir",
            "joblib==1.3.2"
        ])
        import joblib
        st.success("✅ joblib installed successfully")
    except Exception as e:
        st.error(f"❌ Failed to install joblib: {str(e)}")
        st.error("Application cannot continue without joblib")
        st.stop()
# 加载模型
try:
    model = joblib.load("model.joblib")
    st.success("✅ Model loaded successfully")
except Exception as e:
    st.error(f"❌ Failed to load model: {str(e)}")
    st.error("Please ensure 'model.joblib' exists in the root directory")
    st.stop()

# 变量配置（保持原有内容）
VARIABLE_CONFIG = {
    "Sex": {
        "min": 0, 
        "max": 1,
        "description": "Patient gender (0=Female, 1=Male)",
        "value": 0
    },
    # ... 其他变量配置不变 ...
}

# 应用界面（保持原有内容）
st.title("Unplanned Reoperation Risk Prediction System")
st.markdown("---")

# ... 输入表单和预测逻辑保持不变 ...

# 诊断信息
with st.expander("Environment Diagnostics"):
    st.write("**Python Version:**", sys.version)
    st.write("**System Path:**", sys.path)
    
    try:
        import pkg_resources
        installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
        st.write("**Installed Packages:**")
        st.json(installed_packages)
    except ImportError:
        st.warning("Could not retrieve installed packages list")
    
    st.write("**Current Directory Contents:**")
    try:
        files = os.listdir('.')
        st.write(files)
    except Exception as e:
        st.error(f"Error listing files: {str(e)}")