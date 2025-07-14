# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpqndata(RPackage):
	"""Data for the spqn package

	Bulk RNA-seq from GTEx on 4,000 randomly selected, expressed genes. Data has been processed for co-expression analysis.
	"""
	
	bioc = "spqnData"

	version("1.20.0", commit="8598ef66adb7e32a1375e910ad19fa2f1c29e3b2")
	version("1.14.0", commit="123e5e91725cabeabb352621805f6e21ace7932b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

