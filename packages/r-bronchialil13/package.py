# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBronchialil13(RPackage):
	"""time course experiment involving il13

	derived from CNMC (pepr.cnmcresearch.org) http://pepr.cnmcresearch.org/browse.do?action=list_prj_exp&projectId=95 Human Bronchial Cell line A549
	"""
	
	homepage = "http://www.biostat.harvard.edu/~carey"
	bioc = "bronchialIL13" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bronchialIL13_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/bronchialIL13/bronchialIL13_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="fc033e083b118d852d44340e8e3b66d109d2e34a252225056bea5f0b57480784", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/bronchialIL13_1.40.0.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))

