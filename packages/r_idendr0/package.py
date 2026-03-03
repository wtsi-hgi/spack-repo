# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdendr0(RPackage):
	"""Interactive Dendrograms

	Interactive dendrogram that enables the user to select and
    color clusters, to zoom and pan the dendrogram, and to visualize
    the clustered data not only in a built-in heat map, but also in
    'GGobi' interactive plots and user-supplied plots. 
    This is a backport of Qt-based 'idendro' 
    (<https://github.com/tsieger/idendro>) to base R graphics and 
    Tcl/Tk GUI.
	"""
	
	homepage = "http://github.com/tsieger/idendr0"
	cran = "idendr0" 

	version("1.5.3", md5="82af8c5af33475b4f6bb3a591842f53c", url="https://cran.r-project.org/src/contrib/idendr0_1.5.3.tar.gz")

	depends_on("r-tkrplot", type=("build", "run"))
