# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFigir(RPackage):
	"""Check Validity of FIGI, CUSIP, ISIN, SEDOL

	With the functions in this package you can check the
  validity of the following financial instrument identifiers:
  FIGI (Financial Instrument Global Identifier
  <https://www.openfigi.com/about/figi>),
  CUSIP (Committee on Uniform Security Identification Procedures
  <https://www.cusip.com/identifiers.html#/CUSIP>),
  ISIN (International Securities Identification Number
  <https://www.cusip.com/identifiers.html#/ISIN>),
  SEDOL (Stock Exchange Daily Official List
  <https://www2.lseg.com/SEDOL-masterfile-service-tech-guide-v8.6>).
  You can also calculate the FIGI checksum of 11-character strings,
  which can be useful if you want to create your own FIGI identifiers.
	"""
	
	homepage = "https://github.com/philaris/figir"
	cran = "figir" 

	version("0.1.7.0", md5="3598ab45c4d60e91ca6a467dd7a5c242")

