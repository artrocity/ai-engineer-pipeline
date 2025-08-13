#!/usr/bin/env python3
"""
AI Engineer Learning Program - Cleanup and Recreate Script

This script removes all existing phase-* directories and recreates them
with the correct structure (3 exercises per day).

Run this script in your project directory:
    python cleanup_and_recreate_phases.py
"""

import os
import shutil
from pathlib import Path

def cleanup_and_recreate_phases():
    """Remove all phase-* directories and recreate them cleanly."""
    
    print("🧹 Starting cleanup and recreation of phase directories...")
    
    # First, remove all existing phase-* directories
    current_dir = Path(".")
    phase_dirs = [d for d in current_dir.iterdir() if d.is_dir() and d.name.startswith("phase-")]
    
    if phase_dirs:
        print(f"🗑️  Removing {len(phase_dirs)} existing phase directories:")
        for phase_dir in phase_dirs:
            print(f"   Removing: {phase_dir.name}")
            shutil.rmtree(phase_dir)
        print("✅ Cleanup complete!")
    else:
        print("📂 No existing phase directories found to remove.")
    
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
    
    def create_day_structure(day_path):
        """Create standard structure for each day folder."""
        day_folders = ["theory", "practice", "projects"]
        for folder in day_folders:
            os.makedirs(day_path / folder, exist_ok=True)
            
        # Create template files
        (day_path / "README.md").touch()
        (day_path / "theory" / "notes.md").touch()
        (day_path / "reflections.md").touch()
        
        # Create 3 practice files: 1 for previous knowledge, 2 for current day
        (day_path / "practice" / "exercise_1_prior_knowledge.py").touch()
        (day_path / "practice" / "exercise_2_core_concepts.py").touch()
        (day_path / "practice" / "exercise_3_advanced.py").touch()
        (day_path / "projects" / "mini_project.py").touch()
    
    print("\n🚀 Recreating phase directories with correct structure...")
    
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
    
    print("\n🎉 Phase directories recreated successfully!")
    print("📁 Each day now has the correct structure:")
    print("   📂 theory/")
    print("   📂 practice/")
    print("      📄 exercise_1_prior_knowledge.py")
    print("      📄 exercise_2_core_concepts.py") 
    print("      📄 exercise_3_advanced.py")
    print("   📂 projects/")
    print("      📄 mini_project.py")
    print("\n🚀 Ready to continue with your AI Engineer journey!")

if __name__ == "__main__":
    cleanup_and_recreate_phases()