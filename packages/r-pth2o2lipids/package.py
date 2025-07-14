# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPth2o2lipids(RPackage):
	"""P. tricornutum HPLC-ESI-MS Lipid Data from van Creveld et al. (2015)

	Annotated HPLC-ESI-MS lipid data in positive ionization mode from an experiment in which cultures of the marine diatom Phaeodactylum tricornutum were treated with various concentrations of hydrogen peroxide (H2O2) to induce oxidative stress. The experiment is described in Graff van Creveld, et al., 2015, "Early perturbation in mitochondria redox homeostasis in response to environmental stress predicts cell fate in diatoms," ISME Journal 9:385-395. PtH2O2lipids consists of two objects: A CAMERA xsAnnotate object (ptH2O2lipids$xsAnnotate) and LOBSTAHS LOBSet object (ptH2O2lipids$xsAnnotate$LOBSet). The LOBSet includes putative compound assignments from the default LOBSTAHS database. Isomer annotation is recorded in three other LOBSet slots.
	"""
	
	homepage = "http://dx.doi.org/10.1038/ismej.2014.136"
	bioc = "PtH2O2lipids"

	version("1.34.0", commit="aff5d442be45f74b67c8a1a94f08e06bb5fe017e")
	version("1.28.0", commit="395bc4c10397526c74536fe31ce7564ca7ed18ba")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-lobstahs", type=("build", "run"))

