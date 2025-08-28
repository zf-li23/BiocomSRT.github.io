---
layout: default
title: 健康评估
---

<section class="py-5">
  <div class="container">
    <h1 class="text-center mb-5">健康评估与推荐</h1>
    
    <form id="health-assessment-form">
      <div class="row mb-3">
        <div class="col-md-6">
          <h3>基本信息</h3>
          <div class="mb-3">
            <label for="age" class="form-label">年龄</label>
            <input type="number" class="form-control" id="age" required>
          </div>
          <div class="mb-3">
            <label for="gender" class="form-label">性别</label>
            <select class="form-select" id="gender" required>
              <option value="" selected disabled>请选择</option>
              <option value="male">男</option>
              <option value="female">女</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="height" class="form-label">身高 (cm)</label>
            <input type="number" class="form-control" id="height" step="0.1" required>
          </div>
          <div class="mb-3">
            <label for="weight" class="form-label">体重 (kg)</label>
            <input type="number" class="form-control" id="weight" step="0.1" required>
          </div>
        </div>
        
        <div class="col-md-6">
          <h3>健康状况</h3>
          <div class="mb-3">
            <label for="chronic_diseases" class="form-label">慢性疾病（多选）</label>
            <select multiple class="form-select" id="chronic_diseases">
              <option value="hypertension">高血压</option>
              <option value="diabetes">糖尿病</option>
              <option value="heart_disease">心脏病</option>
              <option value="copd">慢性阻塞性肺疾病</option>
              <option value="arthritis">关节炎</option>
            </select>
            <div class="form-text">按住Ctrl键多选</div>
          </div>
          <div class="mb-3">
            <label for="blood_pressure" class="form-label">血压 (mmHg)</label>
            <input type="text" class="form-control" id="blood_pressure" placeholder="例如: 120/80">
          </div>
          <div class="mb-3">
            <label for="blood_sugar" class="form-label">血糖 (mmol/L)</label>
            <input type="number" class="form-control" id="blood_sugar" step="0.1">
          </div>
          <div class="mb-3">
            <label for="heart_rate" class="form-label">心率 (次/分钟)</label>
            <input type="number" class="form-control" id="heart_rate">
          </div>
        </div>
      </div>
      
      <div class="row mb-3">
        <div class="col-12">
          <h3>生活习惯</h3>
        </div>
        <div class="col-md-4">
          <div class="mb-3">
            <label for="exercise" class="form-label">每周运动时间 (分钟)</label>
            <input type="number" class="form-control" id="exercise">
          </div>
        </div>
        <div class="col-md-4">
          <div class="mb-3">
            <label for="sleep" class="form-label">每日平均睡眠时间 (小时)</label>
            <input type="number" class="form-control" id="sleep" step="0.1">
          </div>
        </div>
        <div class="col-md-4">
          <div class="mb-3">
            <label class="form-label">吸烟习惯</label>
            <div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="smoking" id="smoking_yes" value="yes">
                <label class="form-check-label" for="smoking_yes">是</label>
              </div>
              <div class="form-check form-check-inline">
                <input class="form-check-input" type="radio" name="smoking" id="smoking_no" value="no" checked>
                <label class="form-check-label" for="smoking_no">否</label>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="text-center">
        <button type="submit" class="btn btn-primary btn-lg">提交评估</button>
      </div>
    </form>
    
    <div id="results" class="mt-5" style="display: none;">
      <h2 class="text-center mb-4">评估结果与建议</h2>
      <div class="row">
        <div class="col-md-6">
          <div class="card">
            <div class="card-header bg-primary text-white">
              健康风险分析
            </div>
            <div class="card-body">
              <ul id="risk-analysis"></ul>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-header bg-primary text-white">
              养老方式推荐
            </div>
            <div class="card-body">
              <p id="care-recommendation"></p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="row mt-4">
        <div class="col-12">
          <div class="card">
            <div class="card-header bg-primary text-white">
              个性化健康建议
            </div>
            <div class="card-body">
              <ul id="health-suggestions"></ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<script>
// 表单提交事件处理
document.getElementById('health-assessment-form').addEventListener('submit', function(event) {
  event.preventDefault();
  
  // 获取表单数据
  const formData = {
    age: parseInt(document.getElementById('age').value),
    gender: document.getElementById('gender').value,
    height: parseFloat(document.getElementById('height').value),
    weight: parseFloat(document.getElementById('weight').value),
    chronicDiseases: Array.from(document.getElementById('chronic_diseases').selectedOptions).map(opt => opt.value),
    bloodPressure: document.getElementById('blood_pressure').value,
    bloodSugar: document.getElementById('blood_sugar').value ? parseFloat(document.getElementById('blood_sugar').value) : null,
    heartRate: document.getElementById('heart_rate').value ? parseInt(document.getElementById('heart_rate').value) : null,
    exercise: document.getElementById('exercise').value ? parseInt(document.getElementById('exercise').value) : null,
    sleep: document.getElementById('sleep').value ? parseFloat(document.getElementById('sleep').value) : null,
    smoking: document.querySelector('input[name="smoking"]:checked').value
  };
  
  // 调用评估函数
  const results = simulateAssessment(formData);
  
  // 显示结果
  displayResults(results);
});

// 模拟评估函数
function simulateAssessment(data) {
  // 这里只是模拟一些简单的规则
  const risks = [];
  const suggestions = [];
  
  // 计算BMI
  const bmi = data.weight / Math.pow(data.height / 100, 2);
  if (bmi < 18.5) {
    risks.push('体重过轻');
    suggestions.push('建议增加营养摄入，适当增重');
  } else if (bmi >= 24) {
    risks.push('超重');
    suggestions.push('建议控制饮食，增加运动量');
  }
  
  // 血压分析
  if (data.bloodPressure) {
    const [systolic, diastolic] = data.bloodPressure.split('/').map(Number);
    if (systolic >= 140 || diastolic >= 90) {
      risks.push('高血压风险');
      suggestions.push('建议定期监测血压，减少钠盐摄入');
    }
  }
  
  // 血糖分析
  if (data.bloodSugar !== null) {
    if (data.bloodSugar > 7.0) {
      risks.push('高血糖风险');
      suggestions.push('建议控制糖分摄入，定期监测血糖');
    }
  }
  
  // 运动分析
  if (data.exercise !== null && data.exercise < 150) {
    risks.push('运动不足');
    suggestions.push('建议每周至少进行150分钟中等强度运动');
  }
  
  // 睡眠分析
  if (data.sleep !== null && data.sleep < 7) {
    risks.push('睡眠不足');
    suggestions.push('建议保证每晚7-9小时睡眠');
  }
  
  // 吸烟分析
  if (data.smoking === 'yes') {
    risks.push('吸烟危害健康');
    suggestions.push('建议戒烟或减少吸烟量');
  }
  
  // 养老方式推荐（简单模拟）
  let careRecommendation = '';
  if (data.age >= 80 || risks.length > 3) {
    careRecommendation = '建议考虑机构养老或专业护工服务';
  } else if (data.age >= 70 || risks.length > 1) {
    careRecommendation = '建议社区养老或日间照料服务';
  } else {
    careRecommendation = '建议居家养老，定期健康检查';
  }
  
  return {
    risks,
    careRecommendation,
    suggestions
  };
}

// 显示结果函数
function displayResults(results) {
  const riskList = document.getElementById('risk-analysis');
  riskList.innerHTML = '';
  results.risks.forEach(risk => {
    const li = document.createElement('li');
    li.textContent = risk;
    riskList.appendChild(li);
  });
  
  document.getElementById('care-recommendation').textContent = results.careRecommendation;
  
  const suggestionList = document.getElementById('health-suggestions');
  suggestionList.innerHTML = '';
  results.suggestions.forEach(suggestion => {
    const li = document.createElement('li');
    li.textContent = suggestion;
    suggestionList.appendChild(li);
  });
  
  document.getElementById('results').style.display = 'block';
  
  // 滚动到结果部分
  document.getElementById('results').scrollIntoView({ behavior: 'smooth' });
}
</script>
