# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRflocalfdrData(RPackage):
	"""Data for the Vignette and Examples in 'RFlocalfdr'

	Data for the vignette and examples in 'RFlocalfdr'. Contains a dataset of 1103547 importance values,
       and the table of variables used in the random forest splits. The data is Chromosome 22 taken from Auton et al.
       (2015) <doi:10.1038/nature15393>. It also contains a 51 samples by 22283 genes data set taken from
       Spira et al. (2004) <doi:10.1165/rcmb.2004-0273OC>.
	"""
	
	cran = "RFlocalfdr.data" 

	version("0.0.3", md5="3e927a4483fa7894cfe1ebb14e64b933")

	depends_on("r@2.10:", type=("build", "run"))
