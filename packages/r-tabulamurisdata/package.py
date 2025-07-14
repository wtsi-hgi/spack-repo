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

	version("1.26.0", commit="d4dcd5a406883c6a088e61fb85718291124bba8f")
	version("1.20.0", commit="f4c0e080eee836cea56a3898c0fef7fc4aa9e79c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

