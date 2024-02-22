# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPk4adi(RPackage):
	"""PK for Anesthetic Depth Indicators

	Calculate and compare the prediction probability (PK) values for Anesthetic Depth Indicators.
    The PK values are widely used for measuring the performance of anesthetic depth and were first 
    proposed by the group of Dr. Warren D. Smith in the paper 
    Warren D. Smith; Robert C. Dutton; Ty N. Smith (1996) <doi:10.1097/00000542-199601000-00005> and
    Warren D. Smith; Robert C. Dutton; Ty N. Smith (1996) <doi:10.1002/(SICI)1097-0258(19960615)15:11%3C1199::AID-SIM218%3E3.0.CO;2-Y>.
    The authors provided two 'Microsoft Excel' files in xls format for calculating and comparing PK values.
    This package provides an easy-to-use API for calculating and comparing PK values in R. 
	"""
	
	homepage = "https://www.r-project.org"
	cran = "pk4adi" 

	version("0.1.3.2", md5="660cc03b1d0e46062cc615eedd34c5af")

	depends_on("r-data-table@1.10:", type=("build", "run"))
