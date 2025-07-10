# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdClariomSMouse(RPackage):
	"""Platform Design Info for Affymetrix Clariom_S_Mouse

	Platform Design Info for Affymetrix Clariom_S_Mouse
	"""
	
	bioc = "pd.clariom.s.mouse" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.clariom.s.mouse_3.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.clariom.s.mouse/pd.clariom.s.mouse_3.14.1.tar.gz"]

	version("3.14.1", sha256="f37288faa3234659fd663e18db890e3abea0da5428b14e33d8d052405011cc95")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

