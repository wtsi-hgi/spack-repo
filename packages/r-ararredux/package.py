# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArarredux(RPackage):
	"""Rigorous Data Reduction and Error Propagation of Ar40 / Ar39
Data

	Processes noble gas mass spectrometer data to determine the isotopic composition of argon (comprised of Ar36, Ar37, Ar38, Ar39 and Ar40) released from neutron-irradiated potassium-bearing minerals. Then uses these compositions to calculate precise and accurate geochronological ages for multiple samples as well as the covariances between them. Error propagation is done in matrix form, which jointly treats all samples and all isotopes simultaneously at every step of the data reduction process. Includes methods for regression of the time-resolved mass spectrometer signals to t=0 ('time zero') for both single- and multi-collector instruments, blank correction, mass fractionation correction, detector intercalibration, decay corrections, interference corrections, interpolation of the irradiation parameter between neutron fluence monitors, and (weighted mean) age calculation. All operations are performed on the logs of the ratios between the different argon isotopes so as to properly treat them as 'compositional data', sensu Aitchison [1986, The Statistics of Compositional Data, Chapman and Hall].
	"""
	
	cran = "ArArRedux" 

	version("1.0", md5="f073adaa771c1ce9966dac45691773e2")

	depends_on("r@3.0.2:", type=("build", "run"))
