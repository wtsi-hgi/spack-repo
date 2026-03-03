# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiskscorescvd(RPackage):
	"""Cardiovascular Risk Scores Calculator

	A tool to calculate Cardiovascular Risk Scores in large data frames. Cardiovascular risk scores are statistical tools used to assess an individual's likelihood of developing a cardiovascular disease based on various risk factors, such as age, gender, blood pressure, cholesterol levels, and smoking. Here we bring together the six most commonly used in the emergency department. Using 'RiskScorescvd', you can calculate all the risk scores in an extended dataset in seconds. ASCVD described in Goff, et al (2013) <doi:10.1161/01.cir.0000437741.48606.98>. EDACS described in Mark DG, et al (2016) <doi:10.1016/j.jacc.2017.11.064>. GRACE described in Fox KA, et al (2006) <doi:10.1136/bmj.38985.646481.55>. HEART is described in Mahler SA, et al (2017) <doi:10.1016/j.clinbiochem.2017.01.003>. SCORE2/OP described in SCORE2 working group and ESC Cardiovascular risk collaboration (2021) <doi:10.1093/eurheartj/ehab309>. TIMI described in Antman EM, et al (2000) <doi:10.1001/jama.284.7.835>.
	"""
	
	cran = "RiskScorescvd" 

	version("0.1.0", md5="89921299fe8a3094f01699f0c595ee1d")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-pooledcohort@0.0.1:", type=("build", "run"))
