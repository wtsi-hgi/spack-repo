# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRemss(RPackage):
	"""Refining Evaluation Methodology on Stage System

	T (extent of the primary tumor), N (absence or presence and extent of regional lymph node metastasis) and M (absence or presence of distant metastasis) are three components to describe the anatomical tumor extent. TNM stage is important in treatment decision-making and outcome predicting. The existing oropharyngeal Cancer (OPC) TNM stages have not made distinction of the two sub sites of Human papillomavirus positive (HPV+) and Human papillomavirus negative (HPV-) diseases. We developed novel criteria to assess performance of the TNM stage grouping schemes based on parametric modeling adjusting on important clinical factors. These criteria evaluate the TNM stage grouping scheme in five different measures: hazard consistency, hazard discrimination, explained variation, likelihood difference, and balance. The methods are described in Xu, W., et al. (2015) <https://www.austinpublishinggroup.com/biometrics/fulltext/biometrics-v2-id1014.php>.
	"""
	
	cran = "remss" 

	version("1.0.1", md5="4f7cc68558763fe1ba569c8c7b2c8c4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
