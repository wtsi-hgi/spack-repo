# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexMl(PythonPackage):
	"""Machine learning support for vaex"""
	
	homepage = "https://www.github.com/vaexio/vaex"
	pypi = "vaex-ml/vaex_ml-1.0.0a1-py3-none-any.whl" 

	version("0.1.0", sha256="8db941bda27b5b1362a5bf5f4e61b8099cdec4c97eebae6b3369d8f73731c089")
	version("0.10.0", sha256="35d402c1c57d25779d0b286fdadcff945c51f9b4a476f58b1f1dac05304b5ae0", expand=False, url="https://files.pythonhosted.org/packages/e4/11/a7243d376f40ff1bf0835c14727d2ba6c8512f82a2dfdff699917464cf60/vaex_ml-0.10.0-py3-none-any.whl")
	version("0.11.0", sha256="039acf259859eb5535a92fcba41377b0f879dff2244d479d0103153553fd3d6b", expand=False, url="https://files.pythonhosted.org/packages/12/7e/fc13d69640fb6dc304d740c00f682c4c0c4ef31fa2ccc61020bceefd4b4a/vaex_ml-0.11.0-py3-none-any.whl")
	version("0.11.0a1", sha256="b13aed7d1f8219dc64d4d384b66ed181baa45e31a7d5da77162b5845078c0fdf", expand=False, url="https://files.pythonhosted.org/packages/60/5e/60dc0283871e64c017d3d03ddaaebf2daf45616f0312e88f280a6d31a182/vaex_ml-0.11.0a1-py3-none-any.whl")
	version("0.11.0a2", sha256="16feb0fc759afc0966d2756489387e7ba989b9afb0b93171ce80b00e33045df6", expand=False, url="https://files.pythonhosted.org/packages/a7/70/6141393ddad5a60a700584b0123ca95a911b1a108a13459a488f8db9152d/vaex_ml-0.11.0a2-py3-none-any.whl")
	version("0.11.0a3", sha256="21b343cacd8c1ff1329a0fa5ba65e05bf0f82c8b3474d87c5738a7fed4fa0f52", expand=False, url="https://files.pythonhosted.org/packages/b9/e1/0969ce307a35950e7614a05d207e75de029404508e59bb37269c21297b30/vaex_ml-0.11.0a3-py3-none-any.whl")
	version("0.11.0a4", sha256="41835875003e40f65383a3500a202e9a097ea4a6d16a836103951178c0455dbb", expand=False, url="https://files.pythonhosted.org/packages/11/26/d1a9ab8c6a8a0928eec0e8138a7d21f092112496414946ddc24b01d48c0b/vaex_ml-0.11.0a4-py3-none-any.whl")
	version("0.11.0a5", sha256="91e46dec148825305aaf545d7a05446c71c2faa17ad3e9f78bdd48ed48f71847", expand=False, url="https://files.pythonhosted.org/packages/56/2f/c4d759a98b3cf2c0b07ffb9a9af3b0223cdf035c56d98c991e1277755c45/vaex_ml-0.11.0a5-py3-none-any.whl")
	version("0.11.1", sha256="3e8500df22e6dfb92868cb7e416f1e57a93396e1c13a823c5c8f68144bac4a8b", expand=False, url="https://files.pythonhosted.org/packages/dd/85/f09591b2085e03bf9fc73bb3e867c82defc8bbca38ed243f8132eb50daed/vaex_ml-0.11.1-py3-none-any.whl")
	version("0.12.0", sha256="6322b92572c7e29601e71d1710f1372de2631fa980d868508ea14d8f8ec84224", expand=False, url="https://files.pythonhosted.org/packages/f1/3d/ae1130df00e04dc54d35e817ec2264a429af110db0db0a9ab548831529f8/vaex_ml-0.12.0-py3-none-any.whl")
	version("0.13.0", sha256="f8a71b09a9c86123e47084626c3513aa5d20d38c3b88a9027d356c97bae9263d", expand=False, url="https://files.pythonhosted.org/packages/5c/0f/aef3593c03f8cabe2396242b4c6c713f8eaa20d97d759239cb283deccf1d/vaex_ml-0.13.0-py3-none-any.whl")
	version("0.14.0", sha256="411d83ea00774382b9ff714b5086703b4d965b2c8d2f328a186e844aabcd9885", expand=False, url="https://files.pythonhosted.org/packages/eb/b7/fce622ecbc8d97f0a8a2700f2e9edf26b7cd122c4ab3611c5ed7bf6bb3b9/vaex_ml-0.14.0-py3-none-any.whl")
	version("0.15.0", sha256="9bff1ab7e7920b99292fc7f2b65c8ad895a241fd4f7d90a457100ea9e5921a1f", expand=False, url="https://files.pythonhosted.org/packages/3e/96/f00260ac65b0c22da00a12e951860d7e42fdc22bbe340c3b13d358b9f1b4/vaex_ml-0.15.0-py3-none-any.whl")
	version("0.16.0", sha256="38285570e58f2a06cd05b5268750c5df47812fce1dd4470a9e7d23334f9940c2", expand=False, url="https://files.pythonhosted.org/packages/79/06/90988a52aed0b9947e02da13756efca05b535b6de537106c763fcf7a4e97/vaex_ml-0.16.0-py3-none-any.whl")
	version("0.17.0", sha256="b27d6b12977606eff11d0f745606b081a11a4b4e0588dcc94b310f50a669f194", expand=False, url="https://files.pythonhosted.org/packages/21/62/d32b4e08940d17ef98d22b37fe11036b4cf088a373ffeb9816009abacf6a/vaex_ml-0.17.0-py3-none-any.whl")
	version("0.18.0", sha256="b861794800d46417fad66993dbbee106f51b8760df98477177751e8fd12330e4", expand=False, url="https://files.pythonhosted.org/packages/ad/c6/cd592f0bfb3f5961a1eefc826717b2d5f37cf68ceb77b70a62f75ecdcd46/vaex_ml-0.18.0-py3-none-any.whl")
	version("0.18.1", sha256="bc480eda09bc90875ce8b27d0d001831ea8e44d5a3f30acb1a18e812791250b0", expand=False, url="https://files.pythonhosted.org/packages/7c/73/05a5ec85f42ba4baad0b558c2107a2bb48566eb79149ce61116cfd75fc36/vaex_ml-0.18.1-py3-none-any.whl")
	version("0.18.3", sha256="6d0da072f7268f7a6633e049d12d9056b7b5a4cf8c7a1e4fc1797b948ea2cd88", expand=False, url="https://files.pythonhosted.org/packages/84/43/25be5cefe54b00a25ba330a042ba904c5125bbb1163bd9a4280f90871323/vaex_ml-0.18.3-py3-none-any.whl")
	version("0.2.0", sha256="de368cccb11420a8a010217296ade89aafd2c2a2d9bf1df52b3572f049a72a7c")
	version("0.2.1", sha256="1176bd28fa3ad8f2109753d6466ba05db2c3a7aed308579b30d09ecfc5cc4fc7")
	version("0.2.2", sha256="d7d0be2ef7214ab1d9ea00bb9d82c963a22870c7dd9c1ede2b0cde8be5894f53")
	version("0.2.3", sha256="d8f00ba4539ac8c7b45d9cdd4e78de4e0697debd6eba341a6284deab40036327")
	version("0.2.4", sha256="9c9c1f9696f93f72ff322aa229341ab6c54d3f585c18b66353a3f21c3d206abd")
	version("0.3.0", sha256="c9e559cbe056419d09a9496db8898d589e5097c11d86a32519ad47f8f14ed9bd")
	version("0.3.1", sha256="9243ebf76254f1e10ebc11ed42aa31f36eededb79026d55ec6811437103fa344")
	version("0.3.2", sha256="2112f11bb5fa05122c2342338fc9a432276e895bb8685fb778394c8708099913")
	version("0.5.0", sha256="ae1f2c50c4883e42c99922351f2903ff7ad4078085c606ce7411b0696f88c1f2")
	version("0.6.0", sha256="1f18ef3ec9cc5a7d335d3755b327ae501c8e05d1acf243dbd59b011a8ff194e6")
	version("0.6.1", sha256="cd33e50b34c8426bb88755e62a72af5fa5e809f53b4f9d4bf2c67bfbbef6f453")
	version("0.6.2", sha256="a7b52c96f6453eb3d18ca5a8a99c435ce2adc0338b6dea2a21dc07b529985c7c")
	version("0.7.0", sha256="84a81c51fa63188f854b124433a600d632acaebe66bd92a056ac1b4b886a5d8c")
	version("0.8.0", sha256="ac3da27a272222ff39626104e845b35b0b55b486a8a83535c2f5712e513220cf")
	version("0.9.0", sha256="1078f4a966e438b77bf20c0ae6e21035209f4d2850425b7b77b33e8885f59a01", expand=False, url="https://files.pythonhosted.org/packages/6a/f6/db095215f80aa3591ea074ba539cfaf20e92043ef25af5dd2511bca2d5ec/vaex_ml-0.9.0-py3-none-any.whl")
	version("1.0.0a1", sha256="2228b31d36a27a7557ed53933fe44c291270b699d2e0f3b5f3049309c6773ded", expand=False, url="https://files.pythonhosted.org/packages/22/85/b364c2f3cf41b1f965cf1a0e2facb18e9e43b83a1f1611c1906ce6ca04cf/vaex_ml-1.0.0a1-py3-none-any.whl")

	depends_on("py-jinja2", type=("build", "run"))
	depends_on("py-traitlets", type=("build", "run"))
	depends_on("py-numba", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
