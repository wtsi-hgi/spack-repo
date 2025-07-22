# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMedipsdata(RPackage):
	"""Example data for MEDIPS and QSEA packages

	Example data for MEDIPS and QSEA packages, consisting of chromosome 22 MeDIP and control/Input sample data. Additionally, the package contains MeDIP seq data from 3 NSCLC samples and adjacent normal tissue (chr 20-22). All data has been aligned to human genome hg19.
	"""
	
	bioc = "MEDIPSData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MEDIPSData_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MEDIPSData/MEDIPSData_1.38.0.tar.gz"]

	version("1.38.0", sha256="9530469f60440da51e02d1f5afef51d7b019c7bc7e5464afb5b9639777793dd3")

	depends_on("r@3.5:", type=("build", "run"))

