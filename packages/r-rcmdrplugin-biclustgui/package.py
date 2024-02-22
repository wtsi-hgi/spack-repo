# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginBiclustgui(RPackage):
	"""'Rcmdr' Plug-in GUI for Biclustering

	A plug-in for R Commander ('Rcmdr'). The package is a Graphical
    User Interface (GUI) in which several biclustering methods can be executed,
    followed by diagnostics and plots of the results. Further, the GUI also has
    the possibility to connect the methods to more general diagnostic packages for
    biclustering. Biclustering methods from 'biclust', 'fabia', 's4vd', 'iBBiG',
    'isa2', 'BiBitR', 'rqubic' and 'BicARE' are implemented. Additionally, 'superbiclust' and
    'BcDiag' are also implemented to be able to further investigate results. The
    GUI also provides a couple of extra utilities to export, save, search through
    and plot the results. 'RcmdrPlugin.BiclustGUI' also provides a very specific
    framework for biclustering in which new methods, diagnostics and plots can be
    added. Scripts were prepared so that R-package developers can freely design
    their own dialogs in the GUI which can then be added by the maintainer of
    'RcmdrPlugin.BiclustGUI'. These scripts do not required any knowledge of 'tcltk'
    and 'Rcmdr' and are easy to fill in. (Note: rqubic currently requires manual installation through BiocManager::install('rqubic').)
	"""
	
	cran = "RcmdrPlugin.BiclustGUI" 

	version("1.1.3.1", md5="083c0820eec713266dc7b5352cf5cb5c")

	depends_on("r-biclust", type=("build", "run"))
	depends_on("r-fabia", type=("build", "run"))
	depends_on("r-ibbig", type=("build", "run"))
	depends_on("r-superbiclust@1.1:", type=("build", "run"))
	depends_on("r-bcdiag@1.0.10:", type=("build", "run"))
	depends_on("r-bicare", type=("build", "run"))
	depends_on("r-s4vd", type=("build", "run"))
	depends_on("r-bibitr@0.3.1:", type=("build", "run"))
	depends_on("r-rcmdr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
