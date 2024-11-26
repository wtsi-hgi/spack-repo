# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFlax(PythonPackage):
    """Flax: A neural network library for JAX designed for flexibility"""

    homepage = "https://github.com/google/flax"
    pypi = "flax/flax-0.8.2-py3-none-any.whl"

    version(
        "0.1.0",
        sha256="2f5c21e8006e938fdf37b2748a802403fe13e90d4691e59531c5c2fa2cf5f0d0",
        expand=False,
        url="https://files.pythonhosted.org/packages/13/f6/33d3a8e180787d4540421acf57d8a64175dc23dc29a9125c4f76977b0d75/flax-0.1.0-py3-none-any.whl",
    )
    version(
        "0.1.0rc1",
        sha256="8c7cceaf0a1116aeb38d5a7f4b24d9baea5a9dddfa4fdf87802363ed2b887ea7",
        expand=False,
        url="https://files.pythonhosted.org/packages/8c/5e/b4d781e8a1689ed1b71296be8eaf79e21d3e6e4e473a79b6362e65faed02/flax-0.1.0rc1-py3-none-any.whl",
    )
    version(
        "0.1.0rc2",
        sha256="1d7b093b11efd7faee42262956ad3b62b7ad9c46f59671e6ba7fda5f2efb19f8",
        expand=False,
        url="https://files.pythonhosted.org/packages/0e/8f/6d772aba2fa63aa6c1fd10d267324c44288c1c5705ac971c7d79cea219bb/flax-0.1.0rc2-py3-none-any.whl",
    )
    version(
        "0.2.0",
        sha256="e7f4d0d5cec83dec2bb51f4a35b97422dd23cbb17603d57a9633e17113838c16",
        expand=False,
        url="https://files.pythonhosted.org/packages/91/b8/ab292e363cb8758a391541b7942f175f79b3ac06a477dd4495de7c8c91f6/flax-0.2.0-py3-none-any.whl",
    )
    version(
        "0.2.1",
        sha256="2c872a956af8b8a68f3e889c01f00e1089f2ae8f3ef22cc158938032273c69d7",
        expand=False,
        url="https://files.pythonhosted.org/packages/5f/e8/64d7b23e1394b5fd0461c6dd02c83505d342cdefd3d6268e92e82fa3fbb8/flax-0.2.1-py3-none-any.whl",
    )
    version(
        "0.2.2",
        sha256="e24fd49226e432a44e3796737e9da203c7c41f8303b50fb0bc1c87641a07ffa6",
        expand=False,
        url="https://files.pythonhosted.org/packages/2e/ef/1a0c6a869396e4b20a83375fe06d725b5c1711746578ee8dd6969472af41/flax-0.2.2-py3-none-any.whl",
    )
    version(
        "0.3.0",
        sha256="0ab0269815069f763fd3e387e78d434ac2611fe5bf1cb9b78d64e6ccf44f7591",
        expand=False,
        url="https://files.pythonhosted.org/packages/c7/c0/941b4d2a2164c677fe665b6ddb5ac90306d76f8ffc298f44c41c64b30f1a/flax-0.3.0-py3-none-any.whl",
    )
    version(
        "0.3.1",
        sha256="d1dc79d008b02ea4110f1eaf7e97f1b3e085e45a0bfe62f2f6e26930d3750fdd",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/fb/118294d74ba64e6c12c2f0aadfcfa54e0b44c3d95720ca50284594e770da/flax-0.3.1-py3-none-any.whl",
    )
    version(
        "0.3.2",
        sha256="599073b19e7c6f7091a4e2464c50e99d6eb265725f8bb9d2ceb667ed6237a3cb",
        expand=False,
        url="https://files.pythonhosted.org/packages/35/fb/d2c79c41e776fa0a22b0f9dcc677f60ae5d38a6c24fee9756142ff9104d5/flax-0.3.2-py3-none-any.whl",
    )
    version(
        "0.3.3",
        sha256="974741671a7e3ddddb9b9803605784af0df2e1e9c84fc74eb9a0c54ab4bda0dd",
        expand=False,
        url="https://files.pythonhosted.org/packages/63/1f/63c720200f7a679d9fd408eb2641960d6fa99030c874ecba24091e694f91/flax-0.3.3-py3-none-any.whl",
    )
    version(
        "0.3.4",
        sha256="7c3820d9a556c0fe6d2fcc1175025010d3238e5d2ac6acd8fcc4c27f526941b2",
        expand=False,
        url="https://files.pythonhosted.org/packages/f6/21/21ca1f4831ac24646578d2545c4db9a8369b9da4a4b7dcf067feee312b45/flax-0.3.4-py3-none-any.whl",
    )
    version(
        "0.3.5",
        sha256="7c2c4eefd8576d911d845fe859f5defae288cc264a8353018202d901f7510fa5",
        expand=False,
        url="https://files.pythonhosted.org/packages/83/c6/d6b4f783dee6fe3cb72aa4033bf2073a788ec6f8d661a41320b6d2da33b2/flax-0.3.5-py3-none-any.whl",
    )
    version(
        "0.3.6",
        sha256="8c1c3e181ed7f30aabe761b81bbfad1499173a5480ef5073082183b7469a9f0e",
        expand=False,
        url="https://files.pythonhosted.org/packages/c5/ac/54b106b1bcb8c09bfb0a8480e4793dc97e1eb99006f39f2fa844f864002c/flax-0.3.6-py3-none-any.whl",
    )
    version(
        "0.4.0",
        sha256="9d0ea684fb20f4b2e7562ddcc5a95b6563d085bc567f5bfd3343d37237f4cc30",
        expand=False,
        url="https://files.pythonhosted.org/packages/b6/bc/9c28574d7a064388c796f7c465a21be9242543330e72df122fdfe53644e6/flax-0.4.0-py3-none-any.whl",
    )
    version(
        "0.4.1",
        sha256="eadc0126292bdfdd5ddb21b29c994db18544c6ff4a33eae54d4a59331db5a08f",
        expand=False,
        url="https://files.pythonhosted.org/packages/df/74/6ba8b0be0f7a34b1e96f7e89b14f9a8d89e84ec70557eed97708b3b41d5c/flax-0.4.1-py3-none-any.whl",
    )
    version(
        "0.4.2",
        sha256="37a3293d79cf7b49ca97e2f8fb99b92949013413474e0f059d3b44eec79b5c5a",
        expand=False,
        url="https://files.pythonhosted.org/packages/a8/60/166867abc37237a99b171a40e2d20a12d29e3d07dd2ab1e19caa0d70dc05/flax-0.4.2-py3-none-any.whl",
    )
    version(
        "0.5.0",
        sha256="bff805e587def1efbf53c5f4425bf1a7ce26f2b219cbfeb57d077107b29c91af",
        expand=False,
        url="https://files.pythonhosted.org/packages/cd/1e/7a86dba43abfcc154fea9c577fe49966468b76f118d2f97194572cd1a072/flax-0.5.0-py3-none-any.whl",
    )
    version(
        "0.5.1",
        sha256="0ba5ea6bd1e20956e1da627d36413b43393d10613dd3e1715ad32411ee61dbd5",
        expand=False,
        url="https://files.pythonhosted.org/packages/47/bc/50b6e4804bc04da62cfe5c1fd60082b6dc763959adebb0f39da9bccdef99/flax-0.5.1-py3-none-any.whl",
    )
    version(
        "0.5.2",
        sha256="579bea7d6c8454782a2e0cfd210b26dbaff8afe5d4dd8e6e46c4ea4534cf2831",
        expand=False,
        url="https://files.pythonhosted.org/packages/a3/02/645b49839a59a467370c49004d3ec1cd08a8dc14942cb08da6ee542040a2/flax-0.5.2-py3-none-any.whl",
    )
    version(
        "0.5.3",
        sha256="911dc4d6463ccba9808d303f44dfb4a0a6de277be8f3cbfda1471ed1a3e19374",
        expand=False,
        url="https://files.pythonhosted.org/packages/78/87/1575df3431b552b9e2cf17c3b12876c1a991952b4d3beb962aa2419f74b9/flax-0.5.3-py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="98197d17a82bb239c13d9317508cc4cee8daf8728e8db8fcfbe80277a7dfd9e6",
        expand=False,
        url="https://files.pythonhosted.org/packages/fd/3d/4d137ac1a24733d585045d7a8b56403f4d1d318a9c8765174b2ef14063c9/flax-0.6.0-py3-none-any.whl",
    )
    version(
        "0.6.1",
        sha256="8e06af49089d7befd713a741ac0f9e6d9fb2a64e934d84c2c1b11561b6c0c0d7",
        expand=False,
        url="https://files.pythonhosted.org/packages/c3/e2/9417d8032038b7ca6e06207f0fa201f0a4a3daa0aac424d8f0c8b9041c7f/flax-0.6.1-py3-none-any.whl",
    )
    version(
        "0.6.10",
        sha256="8dccc7b84b00ff6f59a36dc0e79f5919498cfeb009a41f8c07f68bf2513198db",
        expand=False,
        url="https://files.pythonhosted.org/packages/aa/08/eaf561898fed72855051b2ef4b5315bb139a0f5e1fb1f5f7c6a059bfd785/flax-0.6.10-py3-none-any.whl",
    )
    version(
        "0.6.11",
        sha256="3ce6843ed47a35abfd86a7eb47db3934a156d08d6513dc8dcb58d461b0dd6f39",
        expand=False,
        url="https://files.pythonhosted.org/packages/b1/34/c7160278dc751ad0b7c0d3221a6e4ae53c9fcda72a8a2a3e80a522ec10e1/flax-0.6.11-py3-none-any.whl",
    )
    version(
        "0.6.2",
        sha256="9f933c87fb5762fbbf0920531e770bc385f24ef6eeb2f473641591fdbde9de89",
        expand=False,
        url="https://files.pythonhosted.org/packages/ea/4a/3eec1cb959030f950bb4448121b3fe6c7efd3b25c21d51463ea9b542d989/flax-0.6.2-py3-none-any.whl",
    )
    version(
        "0.6.3",
        sha256="0cc0830f76a45c54ebe993aaa751319ea609ca1fb036d418d22259a0074a8759",
        expand=False,
        url="https://files.pythonhosted.org/packages/49/9f/9e6d60664f349d7c3c24c45e6e3c32cd050311e745acde534df992a1eed7/flax-0.6.3-py3-none-any.whl",
    )
    version(
        "0.6.4",
        sha256="fe5010525202241fdc960920033d2e4c0b35f06090c1ad9e280b1f4415ae308f",
        expand=False,
        url="https://files.pythonhosted.org/packages/a8/c8/fae1760e36c5796618df8128a294c838e49b645d2db7e85b4107089e7109/flax-0.6.4-py3-none-any.whl",
    )
    version(
        "0.6.6",
        sha256="bad91854c6e2f975e29ddae838f48e9d685d119c7ce9f464d45e54a8f2945426",
        expand=False,
        url="https://files.pythonhosted.org/packages/97/2b/45bbec832edb5596b75794546e8f52b22793d86253887e26e81f530edd61/flax-0.6.6-py3-none-any.whl",
    )
    version(
        "0.6.7",
        sha256="b4f11553197d3d47385363be24a860ea685ddd968e0c1ab6f6a83c9ba4e93b01",
        expand=False,
        url="https://files.pythonhosted.org/packages/ac/b0/4f70875029d049870774bfa7013f591215b683d398da913ba4ca6cc9ae26/flax-0.6.7-py3-none-any.whl",
    )
    version(
        "0.6.8",
        sha256="221225804c263e39fe3cc8f754dc4192597cb0f063926b2338ea6563604747ed",
        expand=False,
        url="https://files.pythonhosted.org/packages/c9/8f/843602fce11aec76bb28f310f6ec7fd696b7d9ef21b11bd624dd9a654278/flax-0.6.8-py3-none-any.whl",
    )
    version(
        "0.6.9",
        sha256="feb3abd0019b673ffe85b9b286ef59fbb0ecff51707925be77f58038521f8a2f",
        expand=False,
        url="https://files.pythonhosted.org/packages/1f/ee/a6f0a231f2002b46e268f1af6b196b4e35c23a9c0dc20ed54cf3e8cd1706/flax-0.6.9-py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="c63e64124be8011b3d2f65a866d98627a5879f243e18351e85bcd0ab29228fc4",
        expand=False,
        url="https://files.pythonhosted.org/packages/bb/1d/d9dccc3b42aab0713f72f68c0de2b3b58c8a9f81e117fa95e02e66678499/flax-0.7.0-py3-none-any.whl",
    )
    version(
        "0.7.2",
        sha256="261c7b93e6d15ad80e2cedd2edb797d41b0b3c7805a54254de72a2366dc80148",
        expand=False,
        url="https://files.pythonhosted.org/packages/72/a7/147bd0682ff39a4e59352506a7d858e1e003f05a2d96e431fabb8a5491e4/flax-0.7.2-py3-none-any.whl",
    )
    version(
        "0.7.4",
        sha256="84fbcdd70b993bc4a307a140d68d5923d24baadda317ac73d2144977f0ec7d54",
        expand=False,
        url="https://files.pythonhosted.org/packages/5c/69/6aaa77d3fa3599d64527196e0b231476fa2cffc4995675974e22d9df83e9/flax-0.7.4-py3-none-any.whl",
    )
    version(
        "0.7.5",
        sha256="bb8cf313e4935089e222fe676e09ea96e9b4d2f9ad355f8acff37c2ca5640d08",
        expand=False,
        url="https://files.pythonhosted.org/packages/95/a6/5017385e65dee7609250f1dc20c3874289afdf57212e65b7f26411c4313b/flax-0.7.5-py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="945fdf051895f52a81adc46b7bb6640cdd32aaa759428f0fcb6a2e519a46e8bb",
        expand=False,
        url="https://files.pythonhosted.org/packages/4e/f8/73393399a87da4e5284502d353ff95eae28054fe8860c28af171cc789716/flax-0.8.0-py3-none-any.whl",
    )
    version(
        "0.8.1",
        sha256="8cf9ef11859eef252470377556a8cc48db287fc6647407ab34f1fc01461925dd",
        expand=False,
        url="https://files.pythonhosted.org/packages/8d/4a/7e78abc8392ff21b0257deb79e842f80647b63b745447df94893732d60fd/flax-0.8.1-py3-none-any.whl",
    )
    version(
        "0.8.2",
        sha256="911d83e01380fdb3135c309e70981aabd15e7ca038014d7989ddc3cfaf4d0d45",
        expand=False,
        url="https://files.pythonhosted.org/packages/b9/92/59b0a2b5df281206433fa6496b176e95249eb0a8192586f88309d7d5df27/flax-0.8.2-py3-none-any.whl",
    )

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-rich", type=("build", "run"))
    depends_on("py-tensorstore", type=("build", "run"))
    depends_on("py-orbax-checkpoint", type=("build", "run"))
    depends_on("py-optax", type=("build", "run"))
    depends_on("py-msgpack", type=("build", "run"))
    depends_on("py-jax@0.2.13:0.2.25", type=("build", "run"), when="@0.3.4:0.3.5")
    depends_on("py-jax@0.2.21:0.2.25", type=("build", "run"), when="@0.3.6:0.4.0")
    depends_on("py-jax@0.3.0:0.3.23", type=("build", "run"), when="@0.4.1:0.5.0")
    depends_on("py-jax@0.3.2:0.3.23", type=("build", "run"), when="@0.5.1:0.5.3")
    depends_on("py-jax@0.3.16:0.3.23", type=("build", "run"), when="@0.6.0:0.6.4")
    depends_on("py-jax@0.4.2:0.4.3", type=("build", "run"), when="@0.6.6:0.6.7")
    depends_on("py-jax@0.4.19:", type=("build", "run"), when="@0.6.8:")
    depends_on("py-numpy", type=("build", "run"))


# {'numpy(>=1.12)': ['0.1.0', '0.1.0rc2', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], 'jax(>=0.1.59)': ['0.1.0', '0.1.0rc2', '0.2.0', '0.2.1', '0.2.2'], 'matplotlib': ['0.1.0', '0.1.0rc1', '0.1.0rc2', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4', '0.6.6'], 'dataclasses': ['0.1.0', '0.1.0rc1', '0.1.0rc2'], 'msgpack': ['0.1.0', '0.1.0rc1', '0.1.0rc2', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytest;extra=='testing'": ['0.1.0', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytest-xdist;extra=='testing'": ['0.1.0', '0.2.0', '0.8.0', '0.8.1', '0.8.2'], "tensorflow-datasets;extra=='testing'": ['0.1.0', '0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'numpy': ['0.1.0rc1'], 'jaxlib': ['0.1.0rc1'], 'jax': ['0.1.0rc1'], 'jaxlib(>=0.1.41)': ['0.1.0rc2'], 'dataclasses;python_version<"3.7"': ['0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6'], "jaxlib;extra=='testing'": ['0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytest-cov;extra=='testing'": ['0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "tensorflow;extra=='testing'": ['0.2.0', '0.2.1', '0.2.2', '0.3.0', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytest-xdist(==1.34.0);extra=='testing'": ['0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], "svn;extra=='testing'": ['0.2.1', '0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1'], "atari-py;extra=='testing'": ['0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4'], "gym;extra=='testing'": ['0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4'], "ml-collections;extra=='testing'": ['0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "opencv-python;extra=='testing'": ['0.2.2', '0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'jax(>=0.2.6)': ['0.3.0', '0.3.1', '0.3.2', '0.3.3'], "clu;extra=='testing'": ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytype;extra=='testing'": ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "sentencepiece;extra=='testing'": ['0.3.0', '0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "tensorflow-text;extra=='testing'": ['0.3.0'], "tensorflow-cpu(>=2.4.0);extra=='testing'": ['0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6'], "tensorflow-text(>=2.4.0);extra=='testing'": ['0.3.1', '0.3.2', '0.3.3', '0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4'], 'jax(>=0.2.13)': ['0.3.4', '0.3.5'], 'optax': ['0.3.4', '0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "tensorflow(==2.4.1);extra=='testing'": ['0.3.4', '0.3.5', '0.3.6'], "atari-py(==0.2.5);extra=='testing'": ['0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9'], "gym(==0.18.3);extra=='testing'": ['0.3.5', '0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9'], "pytype(==2021.5.25);extra=='testing'": ['0.3.5', '0.3.6', '0.4.0', '0.4.1'], 'jax(>=0.2.21)': ['0.3.6', '0.4.0'], "jraph;extra=='testing'": ['0.3.6', '0.4.0', '0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3'], 'jax(>=0.3)': ['0.4.1', '0.4.2', '0.5.0'], "torch;extra=='testing'": ['0.4.1', '0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'typing-extensions(>=4.1.1)': ['0.4.2', '0.5.0', '0.5.1', '0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], "pandas;extra=='testing'": ['0.5.0', '0.5.1', '0.5.2', '0.5.3'], 'jax(>=0.3.2)': ['0.5.1', '0.5.2', '0.5.3'], 'rich(~=11.1.0)': ['0.5.1'], 'rich(~=11.1)': ['0.5.2', '0.5.3', '0.6.0'], 'PyYAML(>=5.4.1)': ['0.5.2', '0.5.3', '0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], 'tensorstore': ['0.5.3', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'jax(>=0.3.16)': ['0.6.0', '0.6.1', '0.6.2', '0.6.3', '0.6.4'], "jraph(>=0.0.6dev0);extra=='testing'": ['0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], "pytest-custom-exit-code;extra=='testing'": ['0.6.0', '0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'rich(>=11.1)': ['0.6.1', '0.6.10', '0.6.11', '0.6.2', '0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], 'jax(>=0.4.2)': ['0.6.10', '0.6.11', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], 'orbax-checkpoint': ['0.6.10', '0.6.11', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "matplotlib;extra=='all'": ['0.6.10', '0.6.11', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "einops;extra=='testing'": ['0.6.10', '0.6.11', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "mypy;extra=='testing'": ['0.6.10', '0.6.11', '0.6.4', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "tensorflow-text(>=2.11.0);extra=='testing'": ['0.6.10', '0.6.11', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0'], "nbstripout;extra=='testing'": ['0.6.10', '0.6.11', '0.6.6', '0.6.7', '0.6.8', '0.6.9', '0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'orbax': ['0.6.3', '0.6.4', '0.6.6', '0.6.7', '0.6.8'], "gymnasium[accept-rom-license,atari];extra=='testing'": ['0.7.0', '0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'numpy>=1.12': ['0.7.2', '0.7.4'], 'jax>=0.4.2': ['0.7.2', '0.7.4'], 'rich>=11.1': ['0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'typing-extensions>=4.1.1': ['0.7.2'], 'PyYAML>=5.4.1': ['0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "jraph>=0.0.6dev0;extra=='testing'": ['0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pytest-xdist==1.34.0;extra=='testing'": ['0.7.2', '0.7.4', '0.7.5'], "tensorflow-text>=2.11.0;extra=='testing'": ['0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "black[jupyter]==23.7.0;extra=='testing'": ['0.7.2', '0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], "pyink==23.5.0;extra=='testing'": ['0.7.2', '0.7.4'], 'typing-extensions>=4.2': ['0.7.4', '0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'numpy>=1.22': ['0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'jax>=0.4.19': ['0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'numpy>=1.23.2;python_version>="3.11"': ['0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'numpy>=1.26.0;python_version>="3.12"': ['0.7.5', '0.8.0', '0.8.1', '0.8.2'], 'clu<=0.0.9;(python_version<"3.10")andextra==\'testing\'': ['0.7.5', '0.8.0', '0.8.1', '0.8.2']}
