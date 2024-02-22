# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMap(RPackage):
	"""Multimodal Automated Phenotyping

	Electronic health records (EHR) linked with biorepositories are 
    a powerful platform for translational studies. A major bottleneck exists 
    in the ability to phenotype patients accurately and efficiently. 
    Towards that end, we developed an automated high-throughput 
    phenotyping method integrating International 
    Classification of Diseases (ICD) codes and narrative data extracted 
    using natural language processing (NLP). Specifically, our proposed method, 
    called MAP (Map Automated Phenotyping algorithm), fits an ensemble of latent 
    mixture models on aggregated ICD and NLP counts along with healthcare 
    utilization. The MAP algorithm yields a predicted probability of phenotype 
    for each patient and a threshold for classifying subjects with phenotype 
    yes/no (See Katherine P. Liao, et al. (2019) <doi:10.1101/587436>.).
	"""
	
	cran = "MAP" 

	version("0.1.3", md5="2ca031891d0a77e3e0d8e2aae9d230cd")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-flexmix@2.3.14:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
