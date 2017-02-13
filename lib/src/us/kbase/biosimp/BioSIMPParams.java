
package us.kbase.biosimp;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: BioSIMPParams</p>
 * <pre>
 * Insert your typespec information here.
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "workspace_name",
    "fbamodel_id",
    "media",
    "fbaOuptut_id"
})
public class BioSIMPParams {

    @JsonProperty("workspace_name")
    private String workspaceName;
    @JsonProperty("fbamodel_id")
    private String fbamodelId;
    @JsonProperty("media")
    private String media;
    @JsonProperty("fbaOuptut_id")
    private String fbaOuptutId;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("workspace_name")
    public String getWorkspaceName() {
        return workspaceName;
    }

    @JsonProperty("workspace_name")
    public void setWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
    }

    public BioSIMPParams withWorkspaceName(String workspaceName) {
        this.workspaceName = workspaceName;
        return this;
    }

    @JsonProperty("fbamodel_id")
    public String getFbamodelId() {
        return fbamodelId;
    }

    @JsonProperty("fbamodel_id")
    public void setFbamodelId(String fbamodelId) {
        this.fbamodelId = fbamodelId;
    }

    public BioSIMPParams withFbamodelId(String fbamodelId) {
        this.fbamodelId = fbamodelId;
        return this;
    }

    @JsonProperty("media")
    public String getMedia() {
        return media;
    }

    @JsonProperty("media")
    public void setMedia(String media) {
        this.media = media;
    }

    public BioSIMPParams withMedia(String media) {
        this.media = media;
        return this;
    }

    @JsonProperty("fbaOuptut_id")
    public String getFbaOuptutId() {
        return fbaOuptutId;
    }

    @JsonProperty("fbaOuptut_id")
    public void setFbaOuptutId(String fbaOuptutId) {
        this.fbaOuptutId = fbaOuptutId;
    }

    public BioSIMPParams withFbaOuptutId(String fbaOuptutId) {
        this.fbaOuptutId = fbaOuptutId;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((("BioSIMPParams"+" [workspaceName=")+ workspaceName)+", fbamodelId=")+ fbamodelId)+", media=")+ media)+", fbaOuptutId=")+ fbaOuptutId)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
