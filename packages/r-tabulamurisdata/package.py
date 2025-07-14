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

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="f3e8482daac6c4069cd3744a1b7222baac2ffb3b52d8834ce8d3aecfdff617dc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

