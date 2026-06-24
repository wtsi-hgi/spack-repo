# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDjEmailUrl(PythonPackage):
	"""Use an URL to configure email backend settings in your Django Application."""
	
	homepage = "https://github.com/migonzalvar/dj-email-url"
	pypi = "dj-email-url/dj_email_url-1.0.6-py2.py3-none-any.whl" 

	version("0.0.1", sha256="8444db73d93e1c6d406d8e8e7251493f0d690b572f6e7060acff549bf5f087d6")
	version("0.0.10", sha256="25f94c6eeb685b9a574051c68399f9ab9bb26076fd58d15ccc60f3fc525aea4f", expand=False, url="https://files.pythonhosted.org/packages/33/62/79da50ed52b2fcf4178fac1ed28d275bdff4f0a9b112905093d8c054a739/dj_email_url-0.0.10-py2.py3-none-any.whl")
	version("0.0.2", sha256="8dc26d22f23fae2c1edcb1417491470aa79909e5818074a240c471d48f0b7cd8")
	version("0.0.3", sha256="601e5df8686159c109555aa2170f88e058c02ccab4530ffc794741184f163352", expand=False, url="https://files.pythonhosted.org/packages/2d/61/ee290bce66e13efb8450e82a53ebbc81748e39a44e00b1373a07bc51b573/dj_email_url-0.0.3-py2-none-any.whl")
	version("0.0.4", sha256="c4a62a75499183cc645f060785760946dd422000dffbcaa264953b1abd6e5255", expand=False, url="https://files.pythonhosted.org/packages/87/4c/9c6af575c577f6d6d8d1a867c8b7967ea7758ec8c145f12f37687b1a4cec/dj_email_url-0.0.4-py2-none-any.whl")
	version("0.0.5", sha256="954890dc915cc3907a135d95fb0cbd0674361ce09a616ab79c8792c3aaaf5030", expand=False, url="https://files.pythonhosted.org/packages/9e/2f/f24c07d43217dcd9cd0be9669f324ab9c2586311b928eaa3ea6aec92780b/dj_email_url-0.0.5-py2.py3-none-any.whl")
	version("0.0.6", sha256="2da376e4400534bcc837e2b082518ea8385fb24a03cf45599af561607722ec17", expand=False, url="https://files.pythonhosted.org/packages/67/cf/dc40c0815a9fd2db819f4d9d2b809838bc7ea0de67e5554b5db0b3b7996b/dj_email_url-0.0.6-py2.py3-none-any.whl")
	version("0.0.7", sha256="c9f3a430066718efe6ff25de60a2a1affeb517b304f3a3f93ed4389657a4a07e", expand=False, url="https://files.pythonhosted.org/packages/c6/d8/4aa65f7e5078a7eba7fcf0a84f037f76feea0aa27063a3cdf183b690b940/dj_email_url-0.0.7-py2.py3-none-any.whl")
	version("0.0.8", sha256="0cf4142cdda59cd023d56cc50f2d6e425a509eb031f08cff0403175d88131f30", expand=False, url="https://files.pythonhosted.org/packages/54/50/0395d982ecb764221348334b27e76c265ca0fe00de8da53081bbcec5f1bb/dj_email_url-0.0.8-py2.py3-none-any.whl")
	version("0.0.9", sha256="a31900ac8b888969606eadbd6d83a1d1fcc48419c5a37a502600d973afd91386", expand=False, url="https://files.pythonhosted.org/packages/5e/ff/ad79fcf0da072987a755991bf942d54cc2d30ed4c46166737e0487b510c4/dj_email_url-0.0.9-py2.py3-none-any.whl")
	version("0.1.0", sha256="de8e062c1483d1bfc7a9a185c6601f9c822087bd529756989f81f1dc82855cee", expand=False, url="https://files.pythonhosted.org/packages/be/7e/d01d9b0c6f72d49e29eaf427fbae1cfdf184535fc72e8116186175961c28/dj_email_url-0.1.0-py2.py3-none-any.whl")
	version("0.2.0", sha256="136ac43c7f29022130fc4769b4ca8b01cd1c39fedf1659c641c143808182a084", expand=False, url="https://files.pythonhosted.org/packages/84/e5/5804f2d56cf75f91724bb4d3d41411d9092a3e761699c0a67bf3d8aafa14/dj_email_url-0.2.0-py2.py3-none-any.whl")
	version("1.0.0", sha256="19a0450378831e2707e00404866e632837efc67dcc2e7e7a98f72df94b89c1f6", expand=False, url="https://files.pythonhosted.org/packages/20/bc/b2526adaf44314a9737930b45b893a616f2348de5b476ad9f9d7ddcbcd2f/dj_email_url-1.0.0-py2.py3-none-any.whl")
	version("1.0.1", sha256="557c07b3039befdc1c561c4038b155d659c09f996d5e33c91189c2e23969da90", expand=False, url="https://files.pythonhosted.org/packages/ec/38/b72ad5df32978e6d6aba68d678985d00ecedb75552646372bd200d75ee2e/dj_email_url-1.0.1-py2.py3-none-any.whl")
	version("1.0.2", sha256="15148141c6ef123636e4ca3663e95231ed94ca5ed267e91977e5a4397be8b34c", expand=False, url="https://files.pythonhosted.org/packages/3f/45/4ef0d15cc7f148bc6211bc8c6c916f2542842d89ebeaac7f000cf30449f5/dj_email_url-1.0.2-py2.py3-none-any.whl")
	version("1.0.3", sha256="a78b657ffe4094b029ab3e94f42cd82640a135b88a0283885638b969f800dd58", expand=False, url="https://files.pythonhosted.org/packages/2f/51/ee4f48a46dcb8b4b275c245d47b3300ffe362c934f53d0691c5bdd4a50e4/dj_email_url-1.0.3-py2.py3-none-any.whl")
	version("1.0.4", sha256="5a0239560c75749be0de86f17425d4526938fe4d8f3ddff4aa8f98224e44183e", expand=False, url="https://files.pythonhosted.org/packages/0b/e7/9331c74b3a8ed33ee7f845967dde90ac3fcb3b7374ef0878a2745e159db1/dj_email_url-1.0.4-py2.py3-none-any.whl")
	version("1.0.5", sha256="64257c4f9d8139a4af8e5267229d32260e433fbf257b0cf8fc855bb0cc39ca7d", expand=False, url="https://files.pythonhosted.org/packages/cc/5f/52f88123b306a48ea6679d9ea7b1d246fbbd887945baf17099f3b68c30fb/dj_email_url-1.0.5-py2.py3-none-any.whl")
	version("1.0.6", sha256="cbd08327fbb08b104eac160fb4703f375532e4c0243eb230f5b960daee7a96db", expand=False, url="https://files.pythonhosted.org/packages/8a/f9/fcb9745099d821f9a26092d3d6f4df8f10049885045c3a93ff726d2e40a6/dj_email_url-1.0.6-py2.py3-none-any.whl")

