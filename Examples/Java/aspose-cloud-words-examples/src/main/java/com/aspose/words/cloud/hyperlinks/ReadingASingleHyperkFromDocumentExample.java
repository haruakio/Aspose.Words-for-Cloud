package com.aspose.words.cloud.hyperlinks;

import java.io.File;

import com.aspose.storage.api.StorageApi;
import com.aspose.words.api.WordsApi;
import com.aspose.words.cloud.config.Configuration;
import com.aspose.words.model.Hyperlink;
import com.aspose.words.model.HyperlinkResponse;

public class ReadingASingleHyperkFromDocumentExample {
	
	public static void main(String[] argv){
		
         try {
                 // Instantiate Aspose Storage API SDK
                 StorageApi storageApi = new StorageApi(Configuration.apiKey, Configuration.appSID, true);

                 // Instantiate Aspose Words API SDK
                 WordsApi wordsApi = new WordsApi(Configuration.apiKey, Configuration.appSID, true);

                 // set input file name
                 String fileName = "SampleWordDocument.docx";
                 Integer hyperlinkIndex = 0;
                 String storage = null;
                 String folder = null;

                 //upload input file to aspose cloud storage
                 storageApi.PutCreate(fileName, "", "", new File(ReadingASingleHyperkFromDocumentExample.class.getResource("/" + fileName).toURI()));

                 // invoke Aspose.Words Cloud SDK API to get a particular hyperlink in a word document
                 HyperlinkResponse apiResponse = wordsApi.GetDocumentHyperlinkByIndex(fileName, hyperlinkIndex, storage, folder);

                 if (apiResponse != null
                                 && apiResponse.getStatus().equals("OK")) {

                         Hyperlink hyperlink = apiResponse.getHyperlink();

                                 if(hyperlink !=null){
                                         //display the hyperlink info
                                         System.out.println("Display Text: " + hyperlink.getDisplayText() + " Value: " + hyperlink.getValue() + " link: " + hyperlink.getLink().getHref());
                                 }
                 }

         } catch (Exception e) {
                 e.printStackTrace();
         }
	}

}
