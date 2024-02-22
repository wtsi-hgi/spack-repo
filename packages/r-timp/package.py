# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTimp(RPackage):
	"""Fitting Separable Nonlinear Models in Spectroscopy and
Microscopy

	A problem solving environment (PSE) for fitting separable
    nonlinear models to measurements arising in physics and chemistry
    experiments, as described by Mullen & van Stokkum (2007)
    <doi:10.18637/jss.v018.i03> for its use in fitting time resolved
    spectroscopy data, and as described by Laptenok et al. (2007)
    <doi:10.18637/jss.v018.i08> for its use in fitting Fluorescence
    Lifetime Imaging Microscopy (FLIM) data, in the study of Förster
    Resonance Energy Transfer (FRET).  `TIMP` also serves as the
    computation backend for the `GloTarAn` software, a graphical user
    interface for the package, as described in Snellenburg et al. (2012)
    <doi:10.18637/jss.v049.i03>.
	"""
	
	homepage = "https://github.com/glotaran/TIMP"
	cran = "TIMP" 

	version("1.13.6", md5="7098a98e3e79285a8ddd7d55c2af5c87")

	depends_on("r-fields@4.1:", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-gclus", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-minpack-lm@1.1.1:", type=("build", "run"))
	depends_on("r-nnls@1.1:", type=("build", "run"))
