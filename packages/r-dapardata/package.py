# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDapardata(RPackage):
	"""Data accompanying the DAPAR and Prostar packages

	Mass-spectrometry based UPS proteomics data sets from Ramus C, Hovasse A, Marcellin M, Hesse AM, Mouton-Barbosa E, Bouyssie D, Vaca S, Carapito C, Chaoui K, Bruley C, Garin J, Cianferani S, Ferro M, Dorssaeler AV, Burlet-Schiltz O, Schaeffer C, Coute Y, Gonzalez de Peredo A. Spiked proteomic standard dataset for testing label-free quantitative software and statistical methods. Data Brief. 2015 Dec 17;6:286-94 and Giai Gianetto, Q., Combes, F., Ramus, C., Bruley, C., Coute, Y., Burger, T. (2016). Calibration plot for proteomics: A graphical tool to visually check the assumptions underlying FDR control in quantitative experiments. Proteomics, 16(1), 29-32.
	"""
	
	homepage = "http://www.prostar-proteomics.org/"
	bioc = "DAPARdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DAPARdata_1.32.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DAPARdata/DAPARdata_1.32.1.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.1", sha256="27436b254cf9817c7c0653dc7e6e0fe939b6b358b4437bc76d595b197ec191c7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-msnbase", type=("build", "run"))

