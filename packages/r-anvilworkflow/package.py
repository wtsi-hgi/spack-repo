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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AnVILWorkflow_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AnVILWorkflow/AnVILWorkflow_1.2.0.tar.gz"]

    version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="b170a2d4b3389a7f5726135596ace4382cf4886cb0c735c20603c4386fbddb97")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-anvil", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
