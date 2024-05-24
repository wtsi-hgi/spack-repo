# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyIpyvue(PythonPackage):
	"""Jupyter widgets base for Vue libraries"""
	
	homepage = "https://github.com/widgetti/ipyvue"
	pypi = "ipyvue/ipyvue-3.0.0a2-py2.py3-none-any.whl" 

	version("0.1.0", sha256="0d640eb7d466a5663a0eae15e70bff4668305ae42f179486391473efc7858281")
	version("1.0.0", sha256="64ac7b789fb677182de5789c363b1d6c139e3f7c24ea20479c6cb699b73ac42c")
	version("1.0.1", sha256="3c4440dc65d615e3c621ac756d28c4785c48468dc0009cda22f28004dc7fc4fd")
	version("1.0.2", sha256="9c5b6c629b1369d3a878c53af9cafc716e78daefa6ebe8e0a3ae292dac00f14e")
	version("1.1.0", sha256="e5d4afe22fce5ea5352fa564f309100985e242d28c68a55d199160b8467d7e9f")
	version("1.10.0", sha256="dc971aa717c87539be9560cc209f5079ab606d90032e4086ee8ebc01a79bfb00", expand=False, url="https://files.pythonhosted.org/packages/04/6e/c50ef830cc3569458f0f23afb5d15c6f582f81de8ea2284dab6df8bf5097/ipyvue-1.10.0-py2.py3-none-any.whl")
	version("1.10.1", sha256="572057b4b003b5a1b8cbe04eef2c41baa561fa74199cd2b9dd76cc4b5f2c5985", expand=False, url="https://files.pythonhosted.org/packages/5f/dc/107a9756ce488fbf4bb2dc8c08a3c4a680c96f2c7476b5014e14e9b71868/ipyvue-1.10.1-py2.py3-none-any.whl")
	version("1.10.2", sha256="c5926f50a90cd090d58dc5ec10afed57e6726c4ba8a51ab1aa6f9f7fcbe284bc", expand=False, url="https://files.pythonhosted.org/packages/a9/f7/5f899dac3dc430921ba7100d189bc90035fc7476d326a5fac07a4bc95059/ipyvue-1.10.2-py2.py3-none-any.whl")
	version("1.11.0", sha256="609bfc886e51349cf54d0169b14d3bfd208f1c0fc9e8071a74e3ce204a3c43ab", expand=False, url="https://files.pythonhosted.org/packages/97/ff/75d0b7cc41c6f18113a5522a73f99595bd967f1d0fe3495cd27e09d6b58a/ipyvue-1.11.0-py2.py3-none-any.whl")
	version("1.11.1", sha256="220371f40bd870df8c3f374c4b357dbc33ee05e55387132b203c70fb44c3b5a3", expand=False, url="https://files.pythonhosted.org/packages/86/94/bba0473f2cc8959058565dba28d95d1c55721bb843534a7e9b2987e7d02a/ipyvue-1.11.1-py2.py3-none-any.whl")
	version("1.2.0", sha256="c2fd59d9980181ee757550c89d44839ce65a0cc712fd33030ae4ee9da4339cbc")
	version("1.2.1", sha256="a79cf059a019ad6250552a21e00201b4138788d892b8e7abefd3034b92bb4b8d")
	version("1.3.0", sha256="2e084becc18f1ef4c175dc576a848bf52e62481db008392f43c4f43dff2d3453")
	version("1.3.1", sha256="4a24cc6f38af7fe73c97b4ad91daab5835715e461b4a4b2a68047c1f513b7706")
	version("1.3.2", sha256="24ed221dcc3878e70daebdbdffdf7fd2b2111164008ba4b5de6785b72eabf91f")
	version("1.3.3", sha256="8d6c4becdc11013be5485fd1fb19741501b0ef030e9bdd6fe4ddd5d1a9c62362")
	version("1.3.4", sha256="009815638f33e67f0fd9cc4fa2087b2faa438e32703877ca14ecf9826508b724")
	version("1.4.0", sha256="489f5e2b3a165e0ace7d716ea4b4f06ef34bbf5bad717e2d3bf475a28c28a385", expand=False, url="https://files.pythonhosted.org/packages/79/39/06f3c438d0d4b7b26b0a601be6b9633953bb94650e0bceac483a6d0dc249/ipyvue-1.4.0-py2.py3-none-any.whl")
	version("1.4.1", sha256="8388cc2188b32a22efe8a5df602661c62b0ce6b8183014ddc483223819a5da9b", expand=False, url="https://files.pythonhosted.org/packages/ab/f6/6e68eb6fc0381e904331f341331a7af387d739967b3e7e8988fdccaca522/ipyvue-1.4.1-py2.py3-none-any.whl")
	version("1.5.0", sha256="10cb0631116100ae04bb1d228c25ae007d2edcfdb0a7f7b2f6611c0c3b27585b", expand=False, url="https://files.pythonhosted.org/packages/a5/8e/327c434451021521b9c25a41042edd2b0653946a9502febb79b318deb302/ipyvue-1.5.0-py2.py3-none-any.whl")
	version("1.6.0", sha256="209e583801e8ec50aa40447bf67d9f924091ec7c92183ece2c29dfd54a8d9a62", expand=False, url="https://files.pythonhosted.org/packages/d7/38/788834e72412945bd334a80970070d679081459434b8de7cffc591e7966d/ipyvue-1.6.0-py2.py3-none-any.whl")
	version("1.6.1", sha256="66031f4b2c96e7a627652e146202a4f9402ccc61d0973ea9a17ece4911058389", expand=False, url="https://files.pythonhosted.org/packages/21/12/acbfbc3b5069893c8d1c9a89ad7cb6fcd84845fd4de54ae6824b3f95e65c/ipyvue-1.6.1-py2.py3-none-any.whl")
	version("1.7.0", sha256="92039bfe6afdec45c93c0aba09e4efd44d64036947b4e3c4011275b4b11b4629", expand=False, url="https://files.pythonhosted.org/packages/4f/c7/4e0f0b2b0652b55149aab245cb5eec073a554724deae30315de7c118dd9d/ipyvue-1.7.0-py2.py3-none-any.whl")
	version("1.8.0", sha256="491b66bf80a3d2d601457e6d3c694acf4de36d2e1d174d4cb96a5c40edd7108a", expand=False, url="https://files.pythonhosted.org/packages/9b/ac/805253dd87452affe76b8291af7e37b0206ee5b9aa2f3295f6c99eda5227/ipyvue-1.8.0-py2.py3-none-any.whl")
	version("1.9.0", sha256="d0f2474c7c0eea1e07fa13c7e865283d58e3ad4189d2d50a964596b397f86241", expand=False, url="https://files.pythonhosted.org/packages/8f/43/7ee448890b2cbbb6e25fb281a5131922a13e47838dc5fbc2f5838ef33aec/ipyvue-1.9.0-py2.py3-none-any.whl")
	version("1.9.1", sha256="b9df601979f3db142df7842e3c486b13fe84d7ade62ce18a478cd4bc4a819e15", expand=False, url="https://files.pythonhosted.org/packages/28/fb/ccaecc3f0ccd4c15865d2197e504d6e1d21a8951240edf45e972ff83ec12/ipyvue-1.9.1-py2.py3-none-any.whl")
	version("1.9.2", sha256="e35979c2ca980c227c681179d9c52fb5c04468c419ff50a23fc719c9239671ca", expand=False, url="https://files.pythonhosted.org/packages/82/c9/9c83d4f315915a7ebe11808394f052c96b55e7a226b22fbcf95b91283bd7/ipyvue-1.9.2-py2.py3-none-any.whl")
	version("3.0.0a1", sha256="989c28be2879051e6df6632767b4ac0bad86673dadb1e66bd7c97e2c8945dabc", expand=False, url="https://files.pythonhosted.org/packages/41/10/90707243173dff00ea21ececdd88686a2e9783aa5748e9a43b43f4aca8c5/ipyvue-3.0.0a1-py2.py3-none-any.whl")
	version("3.0.0a2", sha256="bd15671fd9dd279f2e38814d90cfb83d0e1c354a8092639cdb9115defeb7f6c3", expand=False, url="https://files.pythonhosted.org/packages/3e/dc/527070a54e5d49ec172df113cb16bd381a9fa4c49635b4eb305c0cefbc49/ipyvue-3.0.0a2-py2.py3-none-any.whl")

	depends_on("py-ipywidgets", type=("build", "run"))
