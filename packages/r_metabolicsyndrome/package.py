# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetabolicsyndrome(RPackage):
	"""Diagnosis of Metabolic Syndrome

	The modified Adult Treatment Panel -III guidelines (ATP-III) proposed by American Heart Association (AHA) and National Heart, Lung and Blood Institute (NHLBI) are used widely for the clinical diagnosis of Metabolic Syndrome. The AHA-NHLBI criteria advise using parameters such as waist circumference (WC), systolic blood pressure (SBP), diastolic blood pressure (DBP), fasting plasma glucose (FPG), triglycerides (TG) and high-density lipoprotein cholesterol (HDLC) for diagnosis of metabolic syndrome. Each parameter has to be interpreted based on the proposed cut-offs, making the diagnosis slightly complex and error-prone. This package is developed by incorporating the modified ATP-III guidelines, and it will aid in the easy and quick diagnosis of metabolic syndrome in busy healthcare settings and also for research purposes. The modified ATP-III-AHA-NHLBI criteria for the diagnosis is described by Grundy et al ., (2005) <doi:10.1161/CIRCULATIONAHA.105.169404>.
	"""
	
	homepage = "https://github.com/jagadishramasamy/metsynd"
	cran = "MetabolicSyndrome" 

	version("0.1.3", md5="873df653f47a797eb2fc6732a5b48e15")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
