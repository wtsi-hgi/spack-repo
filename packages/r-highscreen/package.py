# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighscreen(RPackage):
	"""High-Throughput Screening for Plate Based Essays

	Can be used to carry out extraction, normalization, quality control (QC), candidate hits identification and visualization for plate based assays, in drug discovery. The package methods were applied in H. W. Choi et al. "Identification of Novel Mast Cell Activators Using Cell-Based High-Throughput Screening", SLAS Discovery 24(6), 2019. This project was funded by the Division of Allergy, Immunology, and Transplantation, National Institute of Allergy and Infectious Diseases, National Institutes of Health, Department of Health and Human Services, under contract No. HHSN272201400054C entitled "Adjuvant Discovery For Vaccines Against West Nile Virus and Influenza", awarded to Duke University and lead by Drs. Herman Staats and Soman Abraham.
	"""
	
	cran = "highSCREEN" 

	version("0.4", md5="84b8327285112f17387036ac882c6baf")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-gplots@3.0.1:", type=("build", "run"))
