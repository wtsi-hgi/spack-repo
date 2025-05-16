# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMass(RPackage):
	"""Support Functions and Datasets for Venables and Ripley's MASS.

	Functions and datasets to support Venables and Ripley, "Modern Applied
	Statistics with S" (4th edition, 2002)."""

	cran = "MASS"
	version("7.3-65", sha256="b07ef1e3c364ce56269b4a8a7759cc9f87c876554f91293437bb578cfe38172f")
	version("7.3-64", sha256="bf313725b97fcf69fed86d1f70889ea612bfa9095f36aab47181cc76a8cdbb7f")
	version("7.3-63", sha256="ec3e424217a109e78e8e36e88b587ffcb42eaa00eb4e8a819264de0cc7890c0b")
	version("7.3-61", sha256="3144c8bf579dd7b7c47c259728c27f53f53e294e7ed307da434dfd144e800a90")
	version("7.3-60.2", sha256="bb9c6e6747fff6861076758f7db6d3740a6a9c03c12a5a76dc3f816857457e8e")
	version("7.3-60.1", sha256="06c2844890235b3511f7b28596cc487a08e5935b2cf18746d3590377421bb2e7")
	version("7.3-60.0.1", sha256="74df93593029b803d78902c95eddcaa2e7e9ed186ab0be40b56f3f8bfd13adbd")
	version("7.3-59", sha256="454200bec7a52835fbb7f9fe8e01a7aaa728b3ab87b068fc6d900e01c930da5a")
	version("7.3-58.3", sha256="42e5599582dca0d32bc9c709216ddc71df1761af23f11cfa25d582212a5c79ae")
	version("7.3-58.1", sha256="f704e4e2fb131740d023ae1755c925c2e684886a3061b08e26397135f1231420")
	version("7.3-57", sha256="bd8b880105bc1aadb2db699086f74bd92a8611287979a24243187f9d80795a8d")
	version("7.3-55", sha256="65299cbc8f3fd5e09cb3535eabcb3faad2308e01d5ba9422145cc04d7d0c31a4")
	version("7.3-54", sha256="b800ccd5b5c2709b1559cf5eab126e4935c4f8826cf7891253432bb6a056e821")
	version("7.3-53", sha256="41824e70ada302a620226c0f17b1b2c880c6d1a3a100b53bd6df8e8c97e64b38")
	version("7.3-51.5", sha256="464c0615cef01820cde2bb8457e81575d6755ae9b3ac99f3bfaaac47d43d15cc")
	version("7.3-51.4", sha256="844270a2541eaed420871dfb61d681aa67ee57126645fb6b144b436c25698eeb")
	version("7.3-51.3", sha256="5b0e0e7704d43a94b08dcc4b3fe600b9723d1b3e446dd393e82d39ddf66608b6")
	version("7.3-47", sha256="ed44cdabe84fff3553122267ade61d5cc68071c435f7645d36c8f2e4e9f9c6bf")

	depends_on("r@4:", type=("build", "run"), when="@7.3-58-4:")
	depends_on("r@4.4:", type=("build", "run"), when="@7.3-60.1:")
