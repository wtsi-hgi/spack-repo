# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnvilworkflow(RPackage):
	"""Run workflows implemented in Terra/AnVIL workspace

	The AnVIL is a cloud computing resource developed in part by the National Human Genome Research Institute. The main cloud-based genomics platform deported by the AnVIL project is Terra. The AnVILWorkflow package allows remote access to Terra implemented workflows, enabling end-user to utilize Terra/ AnVIL provided resources - such as data, workflows, and flexible/scalble computing resources - through the conventional R functions.
	"""
	
	bioc = "AnVILWorkflow"

	version("1.8.0", commit="aa6e807fa31f6d0933ad35a63e3e890e019e319b")
	version("1.2.0", commit="9f58777ec7baa67debab48b84d52c900245aa2d5")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-anvil", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
