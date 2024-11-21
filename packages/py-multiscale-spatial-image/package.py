# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMultiscaleSpatialImage(PythonPackage):
    """Generate a multiscale, chunked, multi-dimensional spatial image data structure that can be serialized to OME-NGFF."""

    homepage = "https://github.com/spatial-image/multiscale-spatial-image"
    pypi = "multiscale-spatial-image/multiscale_spatial_image-2.0.2-py3-none-any.whl"

    version(
        "0.10.0",
        sha256="936772fd503129c5c924f15a97801c58c754d4da47fa3e1c93b23f886a69b9cd",
        expand=False,
        url="https://files.pythonhosted.org/packages/03/1f/54d56646392c5670d6db07ca79ca75e9fd97903d3a154d4a4ed7e1d8f765/multiscale_spatial_image-0.10.0-py3-none-any.whl",
    )
    version(
        "0.10.1",
        sha256="1945052447bcaf942e6c738cfc6729b52ff0d522f812ec7a2950869a2262d577",
        expand=False,
        url="https://files.pythonhosted.org/packages/1f/70/e13b9c10edd83e09982e665fe4c01025f681831330936d1c034b0083bca4/multiscale_spatial_image-0.10.1-py3-none-any.whl",
    )
    version(
        "0.11.0",
        sha256="4bee3954bf599bc1e18455e0668a6dc8fb7ba6a506d1542b34e4f333f56d1692",
        expand=False,
        url="https://files.pythonhosted.org/packages/0f/6e/ce51ff28505f763f78e44c5199ee7fc3b870a3259837e211cc3223e0f7c8/multiscale_spatial_image-0.11.0-py3-none-any.whl",
    )
    version(
        "0.11.1",
        sha256="a536fea32b63fa9b79305651575a3c387c53fb9a5f7f82024eb50a1bf99fb405",
        expand=False,
        url="https://files.pythonhosted.org/packages/f9/01/e776e294afde3e0dd4a1db6667ba2dce238a368d45b405b01d8cd9fe4516/multiscale_spatial_image-0.11.1-py3-none-any.whl",
    )
    version(
        "0.11.2",
        sha256="a02f542a2f535c4229b64f4624a31d2b5ae9a098401da7743bb95e6a8759d23d",
        expand=False,
        url="https://files.pythonhosted.org/packages/99/3b/9e62694f6bd360a72d7f944cc025de6334ef0ba11a957a8f859b9b14e491/multiscale_spatial_image-0.11.2-py3-none-any.whl",
    )
    version(
        "0.5.0",
        sha256="8a603b290d056a6b7faf4e5e02da9b5349874d4615b4e89514c88b3a5b30f74d",
        expand=False,
        url="https://files.pythonhosted.org/packages/3b/3e/d02228d987e921d87883c3554471de8be7cc567163d0665a51a4432daf92/multiscale_spatial_image-0.5.0-py2.py3-none-any.whl",
    )
    version(
        "0.6.0",
        sha256="2b9f17cab0926a42a773ae865405b1bf5e27345b10ee49f95fd54a5d7c155db0",
        expand=False,
        url="https://files.pythonhosted.org/packages/23/c6/2371c142b1c8f09454ab53fa4714ed140778a7da5b370f9723bc2bade697/multiscale_spatial_image-0.6.0-py2.py3-none-any.whl",
    )
    version(
        "0.7.0",
        sha256="8be48fd6d1d8c30a262f9eabcabd261ad74f29c79165b4a34f8fa3a2fd57bd43",
        expand=False,
        url="https://files.pythonhosted.org/packages/d7/87/c8debf9450d2f30dbc4997e85a13716219d0444c076fac988e1494a2d343/multiscale_spatial_image-0.7.0-py2.py3-none-any.whl",
    )
    version(
        "0.8.0",
        sha256="42bb3b59d160d681396ec69b91bd14a80ea3816bb290142b3259fa2e014d0d42",
        expand=False,
        url="https://files.pythonhosted.org/packages/58/b3/da7c6c733fd78416416ad593951cdf46142514ca103a58e1958c169b4d94/multiscale_spatial_image-0.8.0-py2.py3-none-any.whl",
    )
    version(
        "0.9.0",
        sha256="555a580bd39d247aa017ea32be9f40bca5c63eab8252e2aa449e4662dfe8468a",
        expand=False,
        url="https://files.pythonhosted.org/packages/68/24/4db4dc262b73b41774eef081719e1076d144afbbfa35788eb639513b65d9/multiscale_spatial_image-0.9.0-py2.py3-none-any.whl",
    )
    version(
        "1.0.0",
        sha256="2b1bac6aa12f493ffaa97e6b4395228211b4188f055d18786a82b8db78e00176",
        expand=False,
        url="https://files.pythonhosted.org/packages/e0/5e/68c5e04da4b52595ecaf8bd1ea35bc6047d0cda2abe05c1ba54a84303a60/multiscale_spatial_image-1.0.0-py3-none-any.whl",
    )
    version(
        "1.0.1",
        sha256="e927ed619d23e6b61777ca05a7c50f29db86dcfc2857f512bec6be8bcb351fcf",
        expand=False,
        url="https://files.pythonhosted.org/packages/f5/98/23d67fb3e1cb801122bbf3ced565e796d471a09b610cd9c5697528e83494/multiscale_spatial_image-1.0.1-py3-none-any.whl",
    )
    version(
        "2.0.0",
        sha256="4bcb680ebe8d7ad013b973ca023cbf69b9ec292bf5c96e565ba4dc7c9dbcaa78",
        expand=False,
        url="https://files.pythonhosted.org/packages/70/4b/0e2cea76e5c382444eb4aba7057d8ad5233c95230b00889ab0c20661e769/multiscale_spatial_image-2.0.0-py3-none-any.whl",
    )
    version(
        "2.0.1",
        sha256="8e6d96d600fe23bbe996f0d2f8ed2294b0b23874bbcc5583d51d7222463bd8ba",
        expand=False,
        url="https://files.pythonhosted.org/packages/38/7c/a2454b23d475b12e80f6cf645f03d330a2d49c4af535a1e1306ec1cef85b/multiscale_spatial_image-2.0.1-py3-none-any.whl",
    )
    version(
        "2.0.2",
        sha256="0c25fe7d743293bec06811ccd19842c0998dcdb99b58a0102116340d97d7dfcc",
        expand=False,
        url="https://files.pythonhosted.org/packages/4f/02/eff2e0a291201b70f5c342a8dac0ec67c75aa912af50a999054b99755832/multiscale_spatial_image-2.0.2-py3-none-any.whl",
    )

    depends_on("py-setuptools", type=("build"))
    depends_on("python@3.10:3.13", type=("build", "run"))
    depends_on("py-dask", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-spatial-image", type=("build", "run"))
    depends_on("py-xarray", type=("build", "run"))
    depends_on("py-xarray@2024.10.0:", type=("build", "run"), when="@2.0.0:")
    depends_on("py-xarray-datatree", type=("build", "run"))
    depends_on("py-zarr@2.11:", type=("build", "run"))


# {'dask': ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'numpy': ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'spatial-image>=0.2.1': ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'xarray': ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0', '1.0.0', '1.0.1'], 'xarray-datatree>=0.0.5': ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0', '1.0.0', '1.0.1'], "dask-image;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "fsspec;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "ipfsspec;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "itk-filtering>=5.3rc4;extra=='test'": ['0.10.0'], "jsonschema;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "nbmake;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "pooch;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "pytest;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "pytest-mypy;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "urllib3;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "zarr;extra=='test'": ['0.10.0', '0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0'], "dask-image;extra=='dask-image'": ['0.10.1', '0.11.0', '0.11.1', '0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "itk-filtering>=5.3rc4.post2;extra=='itk'": ['0.10.1', '0.11.0', '0.11.1'], "itk-filtering>=5.3rc4.post2;extra=='test'": ['0.10.1', '0.11.0', '0.11.1'], "itk-filtering>=5.3.0;extra=='itk'": ['0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], "itk-filtering>=5.3.0;extra=='test'": ['0.11.2', '1.0.0', '1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'spatial_image>=0.2.1': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'itk-filtering>=5.3rc4;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'jsonschema;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'pytest;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'pytest-mypy;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'fsspec;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'ipfsspec;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'nbmake;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'zarr;extra=="test"': ['0.5.0', '0.6.0', '0.7.0', '0.8.0', '0.9.0'], 'dask_image;extra=="test"': ['0.7.0', '0.8.0', '0.9.0'], 'python-dateutil': ['1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'zarr': ['1.0.1', '2.0.0', '2.0.1', '2.0.2'], "pyimagej;extra=='imagej'": ['1.0.1', '2.0.0', '2.0.1', '2.0.2'], "matplotlib<4,>=3.9.1;extra=='notebooks'": ['1.0.1'], "ome-types<0.6,>=0.5.1.post1;extra=='notebooks'": ['1.0.1', '2.0.0', '2.0.1', '2.0.2'], "tqdm<5,>=4.66.4;extra=='notebooks'": ['1.0.1', '2.0.0', '2.0.1', '2.0.2'], 'xarray>=2024.10.0': ['2.0.0', '2.0.1', '2.0.2'], "matplotlib<4,>=3.9.2;extra=='notebooks'": ['2.0.0', '2.0.1', '2.0.2']}
