#!/usr/bin/env python3
"""
AI Engineer Learning Program - Project Structure Setup Script

This script creates the complete directory structure for the 6-month
AI Engineer learning program, including all phases, weeks, days, and
project folders.

Run this script in your desired project directory:
    python setup_project_structure.py
"""

import os
from pathlib import Path

def create_directory_structure():
    """Create the complete project directory structure."""
    
    # Base project structure
    base_dirs = [
        "docs",
        "utils", 
        "projects"
    ]
    
    # Phase 1: Foundation Building (Weeks 1-4)
    phase1_structure = {
        "phase-1-foundation": {
            "week-01-python-mastery": [
                "day-01-python-fundamentals",
                "day-02-numpy-computing", 
                "day-03-pandas-manipulation",
                "day-04-matplotlib-visualization",
                "day-05-jupyter-environment"
            ],
            "week-02-mathematical-foundations": [
                "day-01-linear-algebra",
                "day-02-calculus-basics",
                "day-03-statistics-probability", 
                "day-04-information-theory",
                "day-05-optimization-fundamentals"
            ],
            "week-03-data-preprocessing": [
                "day-01-data-cleaning",
                "day-02-feature-engineering",
                "day-03-missing-data",
                "day-04-normalization-standardization", 
                "day-05-exploratory-analysis"
            ],
            "week-04-mlops-basics": [
                "day-01-git-github",
                "day-02-virtual-environments",
                "day-03-docker-basics",
                "day-04-cloud-platforms",
                "day-05-cicd-introduction"
            ]
        }
    }
    
    # Phase 2: ML Core (Weeks 5-12)  
    phase2_structure = {
        "phase-2-ml-core": {
            "week-05-06-supervised-learning": [
                "day-01-linear-logistic-regression",
                "day-02-decision-trees-forests", 
                "day-03-support-vector-machines",
                "day-04-naive-bayes-knn",
                "day-05-ensemble-methods",
                "day-06-advanced-supervised",
                "day-07-hyperparameter-tuning",
                "day-08-model-selection",
                "day-09-classification-project",
                "day-10-regression-project"
            ],
            "week-07-08-unsupervised-learning": [
                "day-01-kmeans-clustering",
                "day-02-hierarchical-clustering",
                "day-03-dbscan-clustering", 
                "day-04-pca-analysis",
                "day-05-tsne-umap",
                "day-06-anomaly-detection",
                "day-07-recommender-systems",
                "day-08-clustering-project",
                "day-09-segmentation-project", 
                "day-10-recommendation-project"
            ],
            "week-09-10-model-evaluation": [
                "day-01-cross-validation",
                "day-02-bias-variance-tradeoff",
                "day-03-performance-metrics",
                "day-04-feature-selection",
                "day-05-model-interpretation",
                "day-06-advanced-evaluation",
                "day-07-ab-testing",
                "day-08-evaluation-framework",
                "day-09-comparison-project",
                "day-10-interpretation-project"
            ],
            "week-11-12-scikit-learn": [
                "day-01-advanced-sklearn-features",
                "day-02-pipeline-creation",
                "day-03-custom-transformers",
                "day-04-advanced-preprocessing",
                "day-05-model-persistence",
                "day-06-sklearn-ecosystem", 
                "day-07-performance-optimization",
                "day-08-production-pipelines",
                "day-09-ml-pipeline-project",
                "day-10-end-to-end-project"
            ]
        }
    }
    
    # Phase 3: Deep Learning (Weeks 13-18)
    phase3_structure = {
        "phase-3-deep-learning": {
            "week-13-14-neural-networks": [
                "day-01-perceptrons-multilayer",
                "day-02-backpropagation-algorithm", 
                "day-03-activation-loss-functions",
                "day-04-tensorflow-keras-basics",
                "day-05-pytorch-fundamentals", 
                "day-06-advanced-training",
                "day-07-regularization-techniques",
                "day-08-optimization-algorithms",
                "day-09-neural-net-from-scratch",
                "day-10-deep-learning-classifier"
            ],
            "week-15-16-cnn": [
                "day-01-cnn-architecture",
                "day-02-convolution-pooling",
                "day-03-popular-architectures", 
                "day-04-transfer-learning",
                "day-05-object-detection",
                "day-06-advanced-cnn",
                "day-07-computer-vision-techniques",
                "day-08-image-classification-project",
                "day-09-object-detection-project",
                "day-10-vision-applications"
            ],
            "week-17-18-rnn-nlp": [
                "day-01-rnn-fundamentals",
                "day-02-lstm-gru-architectures",
                "day-03-text-preprocessing",
                "day-04-word-embeddings", 
                "day-05-sequence-models",
                "day-06-attention-mechanisms",
                "day-07-transformer-introduction",
                "day-08-sentiment-analysis-project",
                "day-09-chatbot-project",
                "day-10-nlp-applications"
            ]
        }
    }
    
    # Phase 4: Modern AI & Production (Weeks 19-24)
    phase4_structure = {
        "phase-4-modern-ai": {
            "week-19-20-transformers": [
                "day-01-transformer-architecture",
                "day-02-bert-gpt-overview", 
                "day-03-huggingface-ecosystem",
                "day-04-fine-tuning-models",
                "day-05-prompt-engineering",
                "day-06-advanced-nlp-applications",
                "day-07-llm-integration",
                "day-08-bert-fine-tuning-project",
                "day-09-llm-application-project", 
                "day-10-transformer-applications"
            ],
            "week-21-generative-ai": [
                "day-01-gans-fundamentals",
                "day-02-variational-autoencoders",
                "day-03-diffusion-models",
                "day-04-advanced-computer-vision",
                "day-05-image-generation-project"
            ],
            "week-22-mlops-production": [
                "day-01-model-versioning-tracking",
                "day-02-model-serving-apis",
                "day-03-monitoring-drift-detection", 
                "day-04-scaling-ml-systems",
                "day-05-production-deployment-project"
            ],
            "week-23-specialized": [
                "day-01-reinforcement-learning",
                "day-02-time-series-forecasting",
                "day-03-advanced-recommenders",
                "day-04-multimodal-ai",
                "day-05-specialized-project"
            ],
            "week-24-capstone": [
                "day-01-capstone-planning",
                "day-02-capstone-design", 
                "day-03-capstone-implementation",
                "day-04-capstone-testing",
                "day-05-capstone-documentation"
            ]
        }
    }
    
    # Project structure 
    project_structure = [
        "project-01-data-dashboard",
        "project-02-math-visualizations", 
        "project-03-eda-pipeline",
        "project-04-deploy-simple-model",
        "project-05-classification-system",
        "project-06-regression-predictor",
        "project-07-customer-segmentation", 
        "project-08-recommendation-engine",
        "project-09-model-comparison-framework",
        "project-10-end-to-end-pipeline",
        "project-11-neural-net-scratch", 
        "project-12-deep-learning-classifier",
        "project-13-image-classifier",
        "project-14-object-detection",
        "project-15-sentiment-analyzer",
        "project-16-chatbot-prototype",
        "project-17-bert-fine-tuning",
        "project-18-llm-application", 
        "project-19-image-generation",
        "project-20-production-ml-system",
        "project-21-specialized-domain",
        "project-22-final-capstone"
    ]
    
    def create_day_structure(day_path):
        """Create standard structure for each day folder."""
        day_folders = ["theory", "practice", "projects"]
        for folder in day_folders:
            os.makedirs(day_path / folder, exist_ok=True)
            
        # Create template files
        (day_path / "README.md").touch()
        (day_path / "theory" / "notes.md").touch()
        (day_path / "reflections.md").touch()
        
        # Create sample practice files
        (day_path / "practice" / "exercise_1.py").touch()
        (day_path / "practice" / "exercise_2.py").touch()
        (day_path / "projects" / "mini_project.py").touch()
    
    def create_project_structure(project_path):
        """Create standard structure for each project folder."""
        project_folders = ["src", "data", "notebooks", "models", "docs"]
        for folder in project_folders:
            os.makedirs(project_path / folder, exist_ok=True)
            
        # Create template files
        (project_path / "README.md").touch()
        (project_path / "requirements.txt").touch()
        (project_path / "src" / "__init__.py").touch()
        (project_path / "src" / "main.py").touch()
        
    print("🚀 Creating AI Engineer Learning Program directory structure...")
    
    # Create base directories
    for dir_name in base_dirs:
        os.makedirs(dir_name, exist_ok=True)
        print(f"✅ Created base directory: {dir_name}")
    
    # Combine all phase structures
    all_phases = {**phase1_structure, **phase2_structure, **phase3_structure, **phase4_structure}
    
    # Create phase and week directories with days
    for phase_name, weeks in all_phases.items():
        phase_path = Path(phase_name)
        os.makedirs(phase_path, exist_ok=True)
        
        # Create completed folder for each phase
        os.makedirs(phase_path / "completed", exist_ok=True)
        
        print(f"✅ Created phase: {phase_name}")
        
        for week_name, days in weeks.items():
            week_path = phase_path / week_name
            os.makedirs(week_path, exist_ok=True)
            print(f"  📅 Created week: {week_name}")
            
            for day_name in days:
                day_path = week_path / day_name
                os.makedirs(day_path, exist_ok=True)
                create_day_structure(day_path)
                print(f"    📝 Created day: {day_name}")
    
    # Create project directories
    projects_path = Path("projects")
    for project_name in project_structure:
        project_path = projects_path / project_name
        os.makedirs(project_path, exist_ok=True)
        create_project_structure(project_path)
        print(f"🎯 Created project: {project_name}")
    
    # Create documentation files
    doc_files = ["learning-log.md", "resources.md", "interview-prep.md"]
    docs_path = Path("docs")
    for doc_file in doc_files:
        (docs_path / doc_file).touch()
    print(f"📚 Created documentation files in docs/")
    
    # Create utility files
    utils_files = ["data_processing.py", "visualization_helpers.py", "model_evaluation.py", "__init__.py"]
    utils_path = Path("utils")
    for util_file in utils_files:
        (utils_path / util_file).touch()
    print(f"🛠️ Created utility files in utils/")
    
    # Create requirements.txt and other root files
    Path("requirements.txt").touch()
    Path("LICENSE").touch()
    Path(".gitignore").touch()
    
    print("\n🎉 Directory structure created successfully!")
    print("\n📋 Next steps:")
    print("1. Initialize git repository: git init")
    print("2. Add remote repository: git remote add origin <your-repo-url>") 
    print("3. Create initial commit: git add . && git commit -m 'Initial project structure'")
    print("4. Start with Phase 1, Week 1, Day 1!")
    print("\n🚀 Ready to begin your AI Engineer journey!")

if __name__ == "__main__":
    create_directory_structure()