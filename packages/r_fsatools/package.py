# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsatools(RPackage):
	"""Fragment Analysis and Capillary Sequencing Tool Kit

	A flexible and interfaced framework for importing, processing and ploting Applied Biosystems data files. Application to Reverse-Transcriptase Multiplex Ligation-dependent Probe Amplification (RT-MLPA) gene-expression profiling and classification is illustrated in Mareschal, Ruminy et al (2015) <doi:10.1016/j.jmoldx.2015.01.007>. Gene-fusion detection and Sanger sequencing are illustrated in Mareschal, Palau et al (2021) <doi:10.1182/bloodadvances.2020002517>. Examples are provided for genotyping applications as well.
	"""
	
	homepage = "https://bioinformatics.ovsa.fr/FSAtools"
	cran = "FSAtools" 

	version("2.0.5", md5="dbda0fe23c50d845bfce93f7bc265886")

	depends_on("r@2.10:", type=("build", "run"))
