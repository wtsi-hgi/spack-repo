# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowworkspacedata(RPackage):
	"""A data package containing two flowJo, one diva xml workspace and the associated fcs files as well as three GatingSets for testing the flowWorkspace, openCyto and CytoML packages.

	The necessary external data to run the flowWorkspace and openCyto vignette is found in this package.
	"""
	
	bioc = "flowWorkspaceData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/flowWorkspaceData_3.14.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/flowWorkspaceData/flowWorkspaceData_3.14.0.tar.gz"]

	version("3.20.0", tag="RELEASE_3_21")
	version("3.14.0", sha256="d85fd772ec55091fbe0d57337fe84ee36225a28d16ad02bc5824b03450d0a072")


