# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreambugs(RPackage):
	"""Parametric Ordinary Differential Equations Model of Growth,
Death, and Respiration of Macroinvertebrate and Algae Taxa

	Numerically solve and plot solutions of a parametric ordinary
        differential equations model of growth, death, and respiration of
        macroinvertebrate and algae taxa dependent on pre-defined environmental
        factors. The model (version 1.0) is introduced in Schuwirth, N. and
        Reichert, P., (2013) <DOI:10.1890/12-0591.1>. This package includes
        model extensions and the core functions introduced and used in
        Schuwirth, N. et al. (2016) <DOI:10.1111/1365-2435.12605>,
        Kattwinkel, M. et al. (2016) <DOI:10.1021/acs.est.5b04068>,
        Mondy, C. P., and Schuwirth, N. (2017) <DOI:10.1002/eap.1530>,
        and Paillex, A. et al. (2017) <DOI:10.1111/fwb.12927>.
	"""
	
	homepage = "https://www.eawag.ch/en/department/siam/projects/streambugs/"
	cran = "streambugs" 

	version("1.4", md5="6a2588dbbbf0ccc0f42ba83f96ce9af4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-desolve@1.20:", type=("build", "run"))
