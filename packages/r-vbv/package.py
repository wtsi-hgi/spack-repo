# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVbv(RPackage):
	"""The Generalized Berlin Method for Time Series Decomposition

	Time series decomposition for univariate time series using the
    "Verallgemeinerte Berliner Verfahren" (Generalized Berlin Method) as
    described in 'Kontinuierliche Messgrößen und Stichprobenstrategien in
    Raum und Zeit mit Anwendungen in den Natur-, Umwelt-, Wirtschafts-
    und Finanzwissenschaften', by
    Hebbel and Steuer, Springer Berlin Heidelberg, 2022
    <doi:10.1007/978-3-662-65638-9>, or
    'Decomposition of Time Series using the Generalised Berlin 
    Method (VBV)' by Hebbel and Steuer, in Jan Beran, Yuanhua Feng, Hartmut
    Hebbel (Eds.): Empirical Economic and Financial Research - Theory,
    Methods and Practice, Festschrift in Honour of Prof. Siegfried Heiler.
    Series: Advanced Studies in Theoretical and Applied Econometrics.
    Springer 2014, p. 9-40.
	"""
	
	cran = "VBV" 

	version("0.6.2", md5="956132231e14f04ca378d871acfc9c0c")

