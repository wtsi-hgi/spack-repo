# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVaexAstro(PythonPackage):
	"""Astronomy related transformations and FITS file support"""
	
	homepage = "https://www.github.com/maartenbreddels/vaex"
	pypi = "vaex-astro/vaex_astro-0.9.3-py3-none-any.whl" 

	version("0.1.5", sha256="778454590111c509623276798c6f7c9f448ec8bcb660bc97239018a9962c6d9b")
	version("0.2.0", sha256="5c351600388de208bedb3383ef1f2ebf15239d39a862aef916fdb0368f1f85f3")
	version("0.3.0", sha256="5576356ae356f5b648ebb95eaa01c59f08fe140ee6131d3c1b9c39e4e460b939")
	version("0.4.0", sha256="86ae50ee9c14c9f6c4bd8e68173cdb146fc9e41eb7ab1a273df821457d543b0e")
	version("0.5.0", sha256="50522860b10b69ec9c4f64360c1f2b84495005f9bc99795f38b7b60643da0176")
	version("0.6.0", sha256="a901f250e73f04071e9a0650b3032e1eac392c53a79ad9626c6d2f9252251a99")
	version("0.6.1", sha256="c27c26df034f6b119258ab1d3b35bc69a702ef2a4309117076f464f0fe04d6a6")
	version("0.7.0", sha256="f00f48d3c6e34eb9f6e462233cb713313b96308015f0f3da7abe6e9c3b47429c", expand=False, url="https://files.pythonhosted.org/packages/6b/43/a34c35d5c8006cb2e845b892913ff50e6ecaa0040465cd76151e3600491d/vaex_astro-0.7.0-py3-none-any.whl")
	version("0.8.0", sha256="3e7ef88ef6b26221b2669b390764a35fd40e28879e50cab4fbe16adf552d286b", expand=False, url="https://files.pythonhosted.org/packages/53/51/2e0325149f66a83da11d0a9c054bf4654a9ee8a0a9519043722552c2b08e/vaex_astro-0.8.0-py3-none-any.whl")
	version("0.8.0.dev1", sha256="d27ebb85dcebdf6b013f928848c2c18951e54e185cdd27c6d156642a85061fe5", expand=False, url="https://files.pythonhosted.org/packages/c4/3b/4ce19e31f6227ba4552dc7194076b3ea0312940cc329e7ddb897f96d0b65/vaex_astro-0.8.0.dev1-py3-none-any.whl")
	version("0.8.0a1", sha256="77ce4e08f55fdb57f8b6313f18a71135d12ead230f627ce57caa0d590c52a40e", expand=False, url="https://files.pythonhosted.org/packages/53/05/e1a5100cf643096911f8f3dad1372bad5d8ae0a52c4a7419cb82654b1f03/vaex_astro-0.8.0a1-py3-none-any.whl")
	version("0.8.1", sha256="d3a7d27fe4200ea42d84ef24f2241c099c0fc2b7eb9c077cd20c7baa84fe35d6", expand=False, url="https://files.pythonhosted.org/packages/f6/b2/4fac7582e87f5e93fb226c2616e03f72c08b1385d034c176e369edf296cb/vaex_astro-0.8.1-py3-none-any.whl")
	version("0.8.2", sha256="22178d297877fb08e63a68461a549323461d411107eb64b84b8306bfad886fee", expand=False, url="https://files.pythonhosted.org/packages/cc/2c/9be42a5a7c6f237d56579b92da3ebd3103c1b29147e02a7b91762f9f64ba/vaex_astro-0.8.2-py3-none-any.whl")
	version("0.8.3", sha256="a573ef435a89a154155a19cd11f0d736f28bf43be17b5118f51fb01230f35058", expand=False, url="https://files.pythonhosted.org/packages/ee/34/7400373c15616e35e936c06d12bdc60b16b3a0944bb40e65857624f35680/vaex_astro-0.8.3-py3-none-any.whl")
	version("0.9.0", sha256="84db0e41ae85e70062e5ff9bf812a419f67dffd8f68878ba196f0eea4b476a21", expand=False, url="https://files.pythonhosted.org/packages/15/f6/640277a463cf5569b55b5c9b81951d9ebfcc8f10e6e2e22feb7c8512a300/vaex_astro-0.9.0-py3-none-any.whl")
	version("0.9.1", sha256="e9e37b254ce8ad0204ce098d43f4aa57df5dcc9a8e76d87c6e4beaaaf898f76a", expand=False, url="https://files.pythonhosted.org/packages/9d/61/b518961707c0edcdefb1bdd5b062f4b7ea6b22b963b625ae4eb4a7cb7dff/vaex_astro-0.9.1-py3-none-any.whl")
	version("0.9.2", sha256="1fe932775cd23e5548654599fd7fe76ba874e4d5ce0520d58df198c361daf724", expand=False, url="https://files.pythonhosted.org/packages/73/d8/57ed529affccf4ec52b443df1003f8ca25d14cd6d0e0ee5b678d2dc7e2f1/vaex_astro-0.9.2-py3-none-any.whl")
	version("0.9.3", sha256="44e6b6b51b80b319f1f7eb1a596cb69ab04e5dc54666e6ad3436e3463954e1b7", expand=False, url="https://files.pythonhosted.org/packages/47/7c/735325e539d38e3fb789456ef40cc0cc39b05877a2050519c6417ef859bc/vaex_astro-0.9.3-py3-none-any.whl")

	depends_on("py-astropy", type=("build", "run"))
	depends_on("py-vaex-core", type=("build", "run"))
