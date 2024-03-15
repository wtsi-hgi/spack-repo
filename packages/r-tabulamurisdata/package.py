# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTabulamurisdata(RPackage):
	"""10x And SmartSeq2 Data From The Tabula Muris Consortium

	Access to processed 10x (droplet) and SmartSeq2 (on FACS-sorted cells) single-cell RNA-seq data from the Tabula Muris consortium (http://tabula-muris.ds.czbiohub.org/).
	"""
	
	bioc = "TabulaMurisData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TabulaMurisData_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TabulaMurisData/TabulaMurisData_1.20.0.tar.gz"]

	version("1.20.0", md5="39c27cc6646ea3bcdb4637a226b219b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment