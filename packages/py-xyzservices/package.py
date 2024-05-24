# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyXyzservices(PythonPackage):
	"""Source of XYZ tiles providers"""
	
	homepage = "https://github.com/geopandas/xyzservices"
	pypi = "xyzservices/xyzservices-2024.4.0-py3-none-any.whl" 

	version("2021.10.0", sha256="6e0fb54cd34896ceedeffb22c5b442641e4a352a62f1e7d246fe12e950356ed4", expand=False, url="https://files.pythonhosted.org/packages/36/4d/957898696cf816f7b0ec2cf53137c937c199a28e13dd2e9d16fd26971d13/xyzservices-2021.10.0-py3-none-any.whl")
	version("2021.11.0", sha256="a1d1edfd4e057d5e3900b4b765718534f5ac69b28cc108834cb152d5e366e678", expand=False, url="https://files.pythonhosted.org/packages/e0/0f/57250278e0993bd72671b213530ff03fb053499b85a17725d035e25cf4af/xyzservices-2021.11.0-py3-none-any.whl")
	version("2021.7", sha256="13175da215adf0714f9f57acdfa325d185f09ef520f62dcad1008dfd40cf9511", expand=False, url="https://files.pythonhosted.org/packages/45/93/571583a5f63177b2911e667abc53cfb85dc834ebfe7d9989cf81efc00831/xyzservices-2021.7-py3-none-any.whl")
	version("2021.7.1", sha256="415d0227b6d23cb9c1a3facc1cf73ec30d0c5f7ebe4cdff95466b8fe1c4a1c53", expand=False, url="https://files.pythonhosted.org/packages/ac/0a/e5ebdb9b97ce0ca7881c8f6198aa18ace2b2cdd551095eeb06bd463c9cbe/xyzservices-2021.7.1-py3-none-any.whl")
	version("2021.7.2", sha256="3e8302ed5a4852647107486ca16e99fc9616cc2511b7c5363c15e1394bee0647", expand=False, url="https://files.pythonhosted.org/packages/ec/aa/0dcc7d4199771644fa6b69e8b642adcb811e1ccbea6e00f3c5961bff3e94/xyzservices-2021.7.2-py3-none-any.whl")
	version("2021.8.0", sha256="9c2bb8986ee031d40257476e8ab6a2e40095f5e5321f11b50aef20c1ce1bf78c", expand=False, url="https://files.pythonhosted.org/packages/0c/99/84deba2347431568f9ac984898731a82b904696ee8f032dd3fc7bede9c86/xyzservices-2021.8.0-py3-none-any.whl")
	version("2021.8.1", sha256="7e084a51df1a5173ea2f5d15c3c604ab2e49e86a3aaadc687371420cae9e134c", expand=False, url="https://files.pythonhosted.org/packages/62/33/18139799a3fcbb43e0fead961c0f14a6f24f76612e05e7ca2b7584098f4d/xyzservices-2021.8.1-py3-none-any.whl")
	version("2021.9.0", sha256="d82e4958da2bb33e4c35923c10cb7e0c30133d57f0a1e9fba5ed8583352ad2b6", expand=False, url="https://files.pythonhosted.org/packages/c1/44/642cf6a32fd213fc14e3832f94367765540ce96b043d54fd68e9ac4d1f85/xyzservices-2021.9.0-py3-none-any.whl")
	version("2021.9.1", sha256="c772944b50ee2ef29fe97efae977dc0da027037bce2b7b61c01e2412c81b5f5a", expand=False, url="https://files.pythonhosted.org/packages/ea/11/80a2908905f1f7d098f1186a25d6a3578869bbe8e244b33ca4ac854e327d/xyzservices-2021.9.1-py3-none-any.whl")
	version("2022.1.0", sha256="77a5de81435cb11887a3d55830b80a1ed7b489bbf22f9b699f8d120a93549e7a", expand=False, url="https://files.pythonhosted.org/packages/bc/8e/7084cc2f378deca5083cdd08a239be6ce75d6a26d31f566525233d3111ef/xyzservices-2022.1.0-py3-none-any.whl")
	version("2022.1.1", sha256="c982874cd00cb9fc0c422a674d50b2813ce0517b42f6ed3b727384e3ac1b8beb", expand=False, url="https://files.pythonhosted.org/packages/4e/94/b861052c06b7006ed76bffa5816b3ef27a1597d1d25bbdea5632ff1fb4ec/xyzservices-2022.1.1-py3-none-any.whl")
	version("2022.2.0", sha256="5451c76b34791a1f8100cb3e1288d3f725bea77ed30c3324b4770a848e932bf1", expand=False, url="https://files.pythonhosted.org/packages/c8/a1/41806e2dba6fed556bad1ca55e7a2f2267f320d71c690c7b4587b48a29f5/xyzservices-2022.2.0-py3-none-any.whl")
	version("2022.3.0", sha256="3ed14caf936309e165675362add0859f2ef4c1ba7de69a8d3a2966f1c4c29732", expand=False, url="https://files.pythonhosted.org/packages/46/7d/2b3e2a593a9410b6a6d9c6d2516ae6050784a4a15045e146414cba06a33e/xyzservices-2022.3.0-py3-none-any.whl")
	version("2022.4.0", sha256="070d055857cb16fa9e3b53a7b948fc09ba5b2b34a6cf91ee4eed7ffca9321e76", expand=False, url="https://files.pythonhosted.org/packages/16/5d/b29f6f8aab6fae9d1f8c5079399603410c98afa06b39a445345cb8141873/xyzservices-2022.4.0-py3-none-any.whl")
	version("2022.6.0", sha256="eb493eb69bde966788f482e1c3608af99ff18fea8885d795ed1ca3b1a8d2e0ec", expand=False, url="https://files.pythonhosted.org/packages/14/13/c36ba2c63f3b04ccc7877dafa176638d483ac9c7520f8523a2b9f7ff2fcc/xyzservices-2022.6.0-py3-none-any.whl")
	version("2022.9.0", sha256="5547b3d6bc06a60561d039fc9ef5fd521d8bea9b6b3d617410fd764b30c6c2bd", expand=False, url="https://files.pythonhosted.org/packages/6c/99/57e0974500e56381564385940488e931f3a6f05041b97834a4c2af83fff9/xyzservices-2022.9.0-py3-none-any.whl")
	version("2023.10.0", sha256="70b9910f6c8e46f6ca92dea21e9b8cf89edf0ead35a870198fb59a7d63579525", expand=False, url="https://files.pythonhosted.org/packages/b1/2b/53fa918ab16998937586f33d14cb00fbf04ead7425c96b665b73b09c7d64/xyzservices-2023.10.0-py3-none-any.whl")
	version("2023.10.1", sha256="6a4c38d3a9f89d3e77153eff9414b36a8ee0850c9e8b85796fd1b2a85b8dfd68", expand=False, url="https://files.pythonhosted.org/packages/82/c3/e06dfa46464cce3eda4b86df8847cab99d9bc545c76807ee689545187a4c/xyzservices-2023.10.1-py3-none-any.whl")
	version("2023.2.0", sha256="8d29c4d7c33b0ad63f54744ec90f68c5a65d7c0d7e498b624b7c076c1d926998", expand=False, url="https://files.pythonhosted.org/packages/f1/76/1d508556ee4c279841c82521aea4e12496367929d88aec6dd3959f080cfa/xyzservices-2023.2.0-py3-none-any.whl")
	version("2023.5.0", sha256="53b923518d1f7ba22ee77c955c1da34716524bf1910737b097d3208f893af0fe", expand=False, url="https://files.pythonhosted.org/packages/f8/54/35fd46df76033b391fa7c88cafa456ba28383f80bb04adf4045c3c94482b/xyzservices-2023.5.0-py3-none-any.whl")
	version("2023.7.0", sha256="88e9cbf22b31a2f9c1b242e2b18690f5c705f0e539c9bfd37a10399e1037731b", expand=False, url="https://files.pythonhosted.org/packages/50/d7/2ca7f65c189aa71b5a9dfeaabc0b4ab8d50bead74a7863428c579737d625/xyzservices-2023.7.0-py3-none-any.whl")
	version("2024.4.0", sha256="b83e48c5b776c9969fffcfff57b03d02b1b1cd6607a9d9c4e7f568b01ef47f4c", expand=False, url="https://files.pythonhosted.org/packages/b7/2c/08768a39947864fcebc19f059b758d8169a2ac183a61361359f56c144f7c/xyzservices-2024.4.0-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
